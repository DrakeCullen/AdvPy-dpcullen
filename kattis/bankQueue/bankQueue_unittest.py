#!/usr/bin/env python3
import unittest
from bankQueue import add_people, choose_best_customers

class BankQueueTest(unittest.TestCase):
    def test_add_people(self):
        people = []
        add_people(people, 5, 2000)
        add_people(people, 2, 600)
        add_people(people, 1, 17000)
        self.assertEqual(people[0].money, 2000, "First person's money is incorrect")
        self.assertEqual(people[0].time, 5, "First person's time is incorrect")
        self.assertEqual(people[2].money, 17000, "Last person's money is incorrect")
    
    def test_choose_between_same_time(self):
        people = []
        add_people(people, 1, 2000)
        add_people(people, 1, 600)
        add_people(people, 0, 17000)
        people.sort()
        self.assertEqual(choose_best_customers(people, 2), 19000, "Incorrect Max profit is found")
    
    def test_one_customer(self):
        people = []
        add_people(people, 0, 100)
        people.sort()
        self.assertEqual(choose_best_customers(people, 1), 100, "Incorrect Max profit is found")
        
    def test_many_customers(self):
        people = []
        add_people(people, 0, 1000)
        add_people(people, 4, 1520)
        add_people(people, 2, 600)
        add_people(people, 4, 10)
        add_people(people, 3, 500)
        add_people(people, 5, 970)
        add_people(people, 1, 320)
        add_people(people, 3, 10)
        add_people(people, 2, 50)
        people.sort()
        self.assertEqual(choose_best_customers(people, 6), 4910, "Incorrect Max profit is found")

if __name__ == "__main__":
    unittest.main(verbosity=2)
