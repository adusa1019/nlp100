#!/usr/bin/env python
# coding=utf-8

import sys


def extract_odd(string):
    return string[0::2]


if __name__ == '__main__':
    print(extract_odd(sys.argv[1]))
