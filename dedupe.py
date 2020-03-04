#!/usr/bin/env python
import os
import argparse

# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Identify words that are repeated in a text file (e.g., ''the the'')')
    parser.add_argument('file', type=str, help='The text file')
    args = parser.parse_args()

    with open(args.file, 'r') as f:

        lines = f.readlines()
        the_line = 0

        while len(lines) > 0:

            current_line = lines.pop(0)
            words = current_line.split()
            the_line += 1

            if len(words) == 0:
                continue

            detected = False
            for w1, w2 in zip(words[:-1], words[1:]):
                if w1 == w2:
                    detected = True

            if len(lines) > 0:
                next_words = lines[0].split()
                if len(next_words) > 0 and words[-1] == next_words[0]:
                    print('------')
                    print('{:4d}:'.format(the_line), current_line[:-1])
                    print('{:4d}:'.format(the_line+1), lines[0][:-1])
                    print('------')
                    detected = False  # do not print twice

            if detected:
                print('------')
                print('{:4d}:'.format(the_line), current_line[:-1])
                print('------')

