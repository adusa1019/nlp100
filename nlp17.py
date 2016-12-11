#!/usr/bin/env python
# coding=utf-8

import numpy

if __name__ == '__main__':
    with open('hightemp.txt', 'r', encoding='utf-8') as file:
        words = numpy.array([line.split() for line in file.readlines()])
        print(set(words[:, 0]))
