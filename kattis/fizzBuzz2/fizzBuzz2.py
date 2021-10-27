#!/usr/bin/env python3
import sys


def get_candidates_and_values():
    return list(map(int, sys.stdin.readline().split(" "))) 

def preprocess_correct_answers(correct_answers):
    for i in range(1001):
        if i % 5 == 0 and i % 3 == 0:
            correct_answers[i] = "fizzbuzz";
        elif i % 3 == 0:
            correct_answers[i] = "fizz";
        elif i % 5 == 0:
            correct_answers[i] = "buzz";
        else:
            correct_answers[i] = str(i);

def calculate_candidate_correct(value_count, correct_answers):
    input = sys.stdin.readline().split()
    total_correct = 0
    i = 1
    for guess in input: 
        if guess == correct_answers[i]:
            total_correct += 1
        i += 1
    return total_correct
        

def find_best_candidate(candidates, value_count, correct_answers):
    best = -1
    best_pos = 0
    for i in range(candidates):
        total_correct = calculate_candidate_correct(value_count, correct_answers)
        if (total_correct > best):
            best = total_correct
            best_pos = i + 1
    return best_pos
        

def main():
    correct_answers = [0] * 1001
    preprocess_correct_answers(correct_answers)
    candidates, value_count = get_candidates_and_values()
    print(find_best_candidate(candidates, value_count, correct_answers))

if __name__ == "__main__":
    main()