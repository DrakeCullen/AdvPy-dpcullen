#!/usr/bin/env python3
import sys


def get_balloon_length():
    return int(sys.stdin.readline())

def read_array(balloon_length):
    return list(map(int, sys.stdin.readline().split(" "))) 

def find_intersections(balloon_array):
    intersections = [0] * 1000001
    arrows_needed = 0
    for balloon in balloon_array:
        if intersections[balloon]:
            intersections[balloon] -= 1
        else:
            arrows_needed += 1
        intersections[balloon - 1] += 1
    return arrows_needed

def main():
    balloon_length = get_balloon_length()
    balloon_array = read_array(balloon_length)
    print(find_intersections(balloon_array))

if __name__ == "__main__":
    main()