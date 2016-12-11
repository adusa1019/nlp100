#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == '__main__':
    with open('hightemp.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_per_file = max(round(len(lines) / int(sys.argv[1])), 1)
        print(num_per_file)
        for i in range(int(sys.argv[1])):
            with open('xa%03d.txt' % i, 'w', encoding='utf-8') as output:
                [
                    output.write(line)
                    for line in lines[i * num_per_file:i * num_per_file +
                                      num_per_file]
                ]
