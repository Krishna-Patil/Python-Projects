#! /Users/Krishna/Python-Projects/Unix-wc-tool-in-python/env/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(
    "Clone of Unix tool wc ",
    "\nwc -c \nwc -l\nwc -w\nwc -m\n",
    "Returns word, line, character, byte count"
)
parser.add_argument('filename')
parser.add_argument('-c', '--count')
parser.add_argument('-l', '--lines')
parser.add_argument('-w', '--words')
parser.add_argument('-m', '--characters')

args = parser.parse_args()

def unix_wc():
    char_count = 0
    words_count = 0
    if args.count:
        print(os.path.getsize(args.count), args.count)
    if args.lines:
        with open(args.lines, 'r') as f:
            lines = len(f.readlines())
        print(lines, args.lines)
    if args.words:
        with open(args.words, 'r') as f:
            for line in f.readlines():
                words_count += len(line.split())
        print(words_count, args.words)
    if args.characters:
        with open(args.characters, 'r') as f:
            for line in f.readlines():
                char_count += len(line)
        print(char_count, args.characters)
    else:
        with open(args.filename, 'r') as f:
            lines = len(f.readlines())
        with open(args.filename, 'r') as f:
            for line in f.readlines():
                words_count += len(line.split())
        print(lines, words_count, os.path.getsize(args.filename), args.filename)

if __name__ == '__main__':
    unix_wc()