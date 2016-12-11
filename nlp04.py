#!/usr/bin/env python
# coding=utf-8

import sys
import re


def get_elements():
    string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
             "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    index_ones = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    words = string.split()
    return [
        word[0] if i + 1 in index_ones else word[0:2]
        for word, i in zip(words, range(len(words)))
    ]


if __name__ == '__main__':
    print(get_elements())
