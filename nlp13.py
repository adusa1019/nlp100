#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    with open('col1.txt', 'r', encoding='utf-8') as input1:
        with open('col2.txt', 'r', encoding='utf-8') as input2:
            [
                print(line1.split()[0] + '\t' + line2.split()[0])
                for line1, line2 in zip(input1.readlines(), input2.readlines())
            ]
