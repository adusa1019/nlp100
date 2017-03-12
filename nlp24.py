#!/usr/bin/env python
# coding=utf-8

import re
from nlp20 import JaWiki


def get_media_file_lines(text):
    return [
        re.search(r'(ファイル|file):(.*?)\|', line).group(2)
        for line in text.split('\n') if re.search(r'(ファイル|file):(.*?)\|', line)
    ]


if __name__ == '__main__':
    print(get_media_file_lines(JaWiki.get_article("イギリス")))
