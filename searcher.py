#!/usr/bin/env python

"""Searcher.py: A python script to filter between 2 points in a file"""

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Victor Palacio"
__email__ = "vpalacio at gmail dot com"

import argparse
parser = argparse.ArgumentParser(description='Python script to filter between 2 points in a file')
parser.add_argument('-file', help='file to search through')
parser.add_argument('-start', help='starting point')
parser.add_argument('-end', help='end point')

args = parser.parse_args()

with open(args.file) as infile:
    copy = False
    for line in infile:
        if line.strip() == args.start:
            copy = True
        elif line.strip() == args.end:
            copy = False
        elif copy:
            print line,
