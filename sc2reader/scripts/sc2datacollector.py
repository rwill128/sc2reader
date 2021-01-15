#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals, division
from os import walk

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
	
	replay_jsons = factory.load_replays('C:/Users/Rick/Documents/StarCraft II/Accounts/333611946/1-S2-1-8022002/Replays/Multiplayer')
	
	for replay in replay_jsons:
		print(replay)


if __name__ == "__main__":
	main()
