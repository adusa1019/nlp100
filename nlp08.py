#!/usr/bin/env python
# coding=utf-8

import sys


def cipher(string):
    return ''.join([
        chr(219 - ord(char)) if 'a' <= char <= 'z' else char for char in string
    ])


if __name__ == '__main__':
    word = sys.argv[1]
    print(word)
    print(cipher(word))
    print(cipher(cipher(word)))
