#!/usr/bin/env python
"""
Program that checks the balance of parenthesis
"""
import argparse


opening = ["{", "(", "["]
closing = ["}", ")", "]"]
pairs = dict(zip(opening, closing))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Attempts to find unbalanced curly braces in a file"
    )
    parser.add_argument("file", type=str, help="The file to check")
    args = parser.parse_args()

    stack = []

    with open(args.file, "r") as f:

        for l, line in enumerate(f.readlines()):
            for c, char in enumerate(line):

                if char in opening:
                    stack.append([char, (l, c)])

                elif char in closing:
                    if len(stack) > 0 and pairs[stack[-1][0]] == char:
                        stack.pop()
                    else:
                        print(f"Mismatch at line:{l+1} char:{c+1}")

    if len(stack) > 0:
        print("Error: couldn't close the following parenthesis:")
        for p, (l, c) in stack:
            print(f"  line:{l+1} char:{c+1}")
