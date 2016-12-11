#!/usr/bin/env python
# coding=utf-8

import os
import sys
import re
from nlp20 import JaWiki


def get_section_title(text):
    ans = []
    for line in filter(lambda x: re.search(r"^=+.+=+$", x), text.split('\n')):
        words = line.split('=')
        index_center = (len(words) - 1) // 2
        ans.append(words[index_center] + ": " + str(index_center - 1))
    return ans


if __name__ == '__main__':
    print(get_section_title(JaWiki.get_article("イギリス")))
