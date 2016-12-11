#!/usr/bin/env python
# coding=utf-8

import json


class JaWiki:
    @staticmethod
    def get_article(name_country):
        return json.loads(
            next(
                filter(
                    lambda x: json.loads(x)["title"] == name_country,
                    open(
                        'jawiki-country.json', 'r', encoding='utf-8'))))[
                            "text"]


if __name__ == '__main__':
    print(JaWiki.get_article("イギリス"))
