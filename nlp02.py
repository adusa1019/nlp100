#!/usr/bin/env python
# coding=utf-8

import sys


def merge2(string1, string2):
    return ''.join([str1 + str2 for str1, str2 in zip(string1, string2)])


if __name__ == '__main__':
    print(merge2(sys.argv[1], sys.argv[2]))
