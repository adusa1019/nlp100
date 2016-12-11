#!/usr/bin/env python
# coding=utf-8

import sys


def reverse(string):
    return string[len(string) - 1:0:-1]


if __name__ == '__main__':
    print(reverse(sys.argv[1]))
