#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == '__main__':
    [
        print(
            line, end='')
        for line in open(
            'hightemp.txt', 'r', encoding='utf-8').readlines()[-int(sys.argv[
                1]):]
    ]
