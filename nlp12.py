#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r', encoding='utf-8') as file:
        with open('col1.txt', 'w', encoding='utf-8') as output1:
            with open('col2.txt', 'w', encoding='utf-8') as output2:
                for line in file.readlines():
                    output1.write(line.split()[0] + '\n')
                    output2.write(line.split()[1] + '\n')
