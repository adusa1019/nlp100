#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r', encoding='utf-8') as file:
        [print(read.replace('\t', ' '), end='') for read in file.readlines()]
