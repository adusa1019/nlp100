#!/usr/bin/env python
# coding=utf-8

import sys
import random


def typo(string):
    return ' '.join([
        word[0] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
        if len(word) > 4 else word for word in string.split()
    ])


if __name__ == '__main__':
    print(typo(sys.argv[1]))
