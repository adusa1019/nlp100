#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
from nlp20 import JaWiki


def remove_markup(dictionary):
    for l in dictionary.keys():
        dictionary[l] = re.sub(r'\'{2,5}', '', dictionary[l])
        dictionary[l] = re.sub(r'\[{2}([^|\]]+?\|)*(.*?)\]{2}', r'\2',
                               dictionary[l])
        dictionary[l] = re.sub(r'\**\{{2}.+?\|.*?\|(.*?)\}{2}', r'\1',
                               dictionary[l])
        dictionary[l] = re.sub(r'<.*>', r'', dictionary[l])
        dictionary[l] = re.sub(r'\[.*\]', r'', dictionary[l])
    return dictionary


def get_template_dict(text, string):
    for content in text.split("}}\n"):
        if content.startswith("{{" + string):
            values = content.split("\n|")
            dictionary = filter(
                lambda x: len(x) > 0,
                map(lambda x: re.findall(r"(.*)\s=\s(.*)", x, re.S), values))
            dictionary = remove_markup({l[0][0]: l[0][1] for l in dictionary})
            return dictionary.items()


if __name__ == '__main__':
    print(get_template_dict(JaWiki.get_article('イギリス'), "基礎情報"))
