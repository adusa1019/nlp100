#!/usr/bin/env python
# coding=utf-8

import sys


class NGrams:
    def __init__(self, string):
        self.string = string

    def n_gram(self, array, n):
        return [''.join(array[i:i + n]) for i in range(len(array) - n + 1)]

    def char_n_gram(self, n):
        return self.n_gram([char for char in self.string.replace(' ', '')], n)

    def word_n_gram(self, n):
        return self.n_gram(self.string.split(), n)


if __name__ == '__main__':
    temp = NGrams(sys.argv[1])
    print(temp.word_n_gram(2))
    print(temp.char_n_gram(2))
