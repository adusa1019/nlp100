#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == '__main__':
    filename = 'hightemp.txt'
    [
        print(
            line, end='')
        for line in open(
            filename, 'r', encoding='utf-8').readlines()[:int(sys.argv[1])]
    ]
