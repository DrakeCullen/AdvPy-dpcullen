#!/usr/bin/env python3
import unittest
from baloni import find_intersections

class BaloniTest(unittest.TestCase):
    def test_one_balloon(self):
        ballon_array = [1]
        self.assertEqual(find_intersections(ballon_array), 1, "Only one arrow is needed!")
    
    def test_two_same_height(self):
        ballon_array = [1, 1]
        self.assertEqual(find_intersections(ballon_array), 2, "Each balloon needs and arrow!")
        
    def test_many_balloons(self):
        ballon_array = [6, 3, 60, 2934, 94, 93, 3, 2, 2, 1093]
        self.assertEqual(find_intersections(ballon_array), 7, "Only 7 arrows are needed!")
    
    def test_all_unique_arrows(self):
        ballon_array = [435, 294, 9234, 5834, 2034, 8432, 94, 234]
        self.assertEqual(find_intersections(ballon_array), 8, "No arrow can hit two balloons!")
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
