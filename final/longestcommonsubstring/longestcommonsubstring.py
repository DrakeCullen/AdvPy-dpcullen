#!/usr/bin/env python3
import sys


def get_num_strings():
    return int(sys.stdin.readline())

def read_strings(num_strings):
    word_list = []
    for i in range(num_strings):
            temp = input()
            word_list.append(temp)
    return word_list

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

def print_longest(num_strings):
    if num_strings != 1:
        word_list = read_strings(num_strings)
        substring = (long_substr(word_list))
        print(len(substring))
    else:
        only_word = input()
        print(len(only_word))

def main():
    num_strings = get_num_strings()
    print_longest(num_strings)

if __name__ == "__main__":
    main()