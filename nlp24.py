#!/usr/bin/env python
# coding=utf-8

import os
import sys
import re
from nlp100.nlp20 import JaWiki


def get_media_file_lines(text):
    return list(filter(lambda x: re.search(r'\[*(ファイル|file).*', x), text.split('\n')))


if __name__ == '__main__':
    print(get_media_file_lines(JaWiki.get_article("イギリス")))
    # print(JaWiki.get_article("イギリス"))
