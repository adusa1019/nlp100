#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r', encoding='utf-8') as file:
        temp = [line.split()[0] for line in file.readlines()]
        print(
            sorted(
                [(p, temp.count(p)) for p in set(temp)],
                key=lambda x: x[1],
                reverse=True))
