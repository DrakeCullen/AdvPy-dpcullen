#!/usr/bin/env python3
import sys


def get_number_length():
    return int(sys.stdin.readline())

def read_array(number_length):
    return list(map(int, sys.stdin.readline().split(" "))) 

def calculate_left_max(number_length, transformed_array):
    maximum_arr = [1e-9] * number_length
    for i in range(1, number_length):
        maximum_arr[i] = max(maximum_arr[i-1], transformed_array[i-1]) 
    return maximum_arr

def calculate_min_right(number_length, transformed_array):
    minimum_arr = [1e9] * number_length
    for i in range(number_length - 2, -1, -1):
        minimum_arr[i] = min(minimum_arr[i+1], transformed_array[i+1]) 
    return minimum_arr

def find_pivots(number_length, minimum_arr, maximum_arr, transformed_array):
    pivots = 0
    for i in range(number_length):
        if maximum_arr[i] < transformed_array[i] and transformed_array[i] < minimum_arr[i]:
            pivots += 1
    return pivots

def main():
    number_length = get_number_length()
    transformed_array = read_array(number_length)
    maximum_arr = calculate_left_max(number_length, transformed_array)
    minimum_arr = calculate_min_right(number_length, transformed_array)
    print(find_pivots(number_length, minimum_arr, maximum_arr, transformed_array))

if __name__ == "__main__":
    main()