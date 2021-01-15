#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals, division
from os import walk
import json
import pymongo
import os.path

import sc2reader
from sc2reader.factories.plugins.replay import toJSON


def main():
	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"path",
		metavar="path",
		type=str,
		nargs=1,
		help="Path to the replay directory.",
	)
	args = parser.parse_args()
	
	factory = sc2reader.factories.SC2Factory()
	factory.register_plugin("Replay", toJSON())
	
	client = pymongo.MongoClient(
		"mongodb+srv://rwill128:xr0X7bNkA5DbBfoA@cluster0.qhpje.mongodb.net/<dbname>?retryWrites=true&w=majority")
	games_database = client.StarCraft2
	
	replay_jsons = factory.load_replays(args.path[0])
	for replay in replay_jsons:
		replay_dictionary = json.loads(replay)
		json_file_path = 'C:/SC2-Replay-JSONS/' + replay_dictionary['filehash'] + '.json'
		
		if not os.path.exists(json_file_path):
			with open(json_file_path, 'w') as file_handle:
				file_handle.write(replay)
				file_handle.close()
		
			games_database.games.insert_one(replay_dictionary)


if __name__ == "__main__":
	main()


#  "C:\SC2-Replay-JSONS"