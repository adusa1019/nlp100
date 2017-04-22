#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
from nlp20 import JaWiki


def get_template_dict(text, string):
    for content in text.split("}}\n"):
        if content.startswith("{{" + string):
            values = content.split("\n|")
            dictionary = filter(
                lambda x: len(x) > 0,
                map(lambda x: re.findall(r"(.*)\s=\s(.*)", x, re.S), values))
            dictionary = {l[0][0]: l[0][1] for l in dictionary}
            return dictionary.items()


if __name__ == '__main__':
    print(get_template_dict(JaWiki.get_article('イギリス'), "基礎情報"))
