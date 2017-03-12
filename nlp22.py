#!/usr/bin/env python
# coding=utf-8

import re
from nlp20 import JaWiki


def get_categories(text):
    return list(
        map(lambda x: x.split(':')[1],
            filter(lambda x: x.startswith("Category"),
                   re.split(r"[\[\]{}|\n]", text))))


if __name__ == '__main__':
    print(get_categories(JaWiki.get_article("イギリス")))
