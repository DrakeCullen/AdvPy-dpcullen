#!/usr/bin/env python3
import sys

class Person:
    def __init__(self, time, money):
        self._time = time
        self._money = money
    
    @property
    def time(self):
        return self._time
    
    @property
    def money(self):
        return self._money
    
    def __lt__(self, other):
        if self._money != other.money:
            return self._money < other.money
        return self._time > other.time


def read_input():
    lineOne = sys.stdin.readline()
    num_people, total_time = map(int, lineOne.split())
    return num_people, total_time


def add_people(people, time, money):
    person = Person(time, money)
    people.append(person)

def read_and_add_people(people, num_people):
    for i in range(num_people):
        person_info = sys.stdin.readline()
        money, time = map(int, person_info.split())
        add_people(people, time, money)
   

def choose_best_customers(people, total_time):
    taken_times = [0] * total_time
    profit = 0
    for i in range(len(people) - 1, -1, -1):
        persons_time = people[i].time
        while(persons_time >= 0):
            if (taken_times[persons_time] == 0):
                taken_times[persons_time] = 1
                profit += people[i].money
                break
            persons_time -= 1
    return profit
                

def main():
    num_people, total_time = read_input()
    people = []
    read_and_add_people(people, num_people)
    people.sort()
    print(choose_best_customers(people, total_time))


if __name__ == "__main__":
    main()