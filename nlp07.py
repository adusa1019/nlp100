#!/usr/bin/env python
# coding=utf-8

import sys


def generate_string(x, y, z):
    return "%s時の%sは%s" % (str(x), str(y), str(z))


if __name__ == '__main__':
    print(generate_string(sys.argv[1], sys.argv[2], sys.argv[3]))
