#!/usr/bin/env python
# coding=utf-8

import sys
import re


def count_word_length(string):
    return [len(word) for word in re.sub(r'[,.]', '', string).split()]


if __name__ == '__main__':
    print(count_word_length(sys.argv[1]))
