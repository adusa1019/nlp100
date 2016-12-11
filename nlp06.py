#!/usr/bin/env python
# coding=utf-8

import sys
import nlp05

if __name__ == '__main__':
    X = set(nlp05.NGrams(sys.argv[1]).char_n_gram(2))
    Y = set(nlp05.NGrams(sys.argv[2]).char_n_gram(2))
    print(X.union(Y))
    print(X.intersection(Y))
    print(X.difference(Y))
    print(Y.difference(X))
    print(sys.argv[3] in X)
    print(sys.argv[3] in Y)
