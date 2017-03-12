#!/usr/bin/env python
# coding=utf-8

import json
import os
import sys
from nlp20 import JaWiki


def get_category_lines(text):
    return list(filter(lambda x: x.startswith("[[Category"), text.split()))


if __name__ == '__main__':
    print(get_category_lines(JaWiki.get_article("イギリス")))
