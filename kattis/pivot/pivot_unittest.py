#!/usr/bin/env python3
import unittest
from pivot import calculate_left_max, calculate_min_right, find_pivots

class PivotTest(unittest.TestCase):
    def test_calculate_left_max(self):
        numbers = [2, 5, 6, 9, 11, 1]
        self.assertEqual(calculate_left_max(6, numbers), [1e-09, 2, 5, 6, 9, 11], "Maximums incorrectly calculated!")
        
    def test_calculate_min_right(self):
        numbers = [6, 2, 5, 1, 9, 11]
        self.assertEqual(calculate_min_right(6, numbers), [1, 1, 1, 9, 11, 1e9], "Minimums incorrectly calculated!")
    
    def test_increasing_order(self):
        numbers = [1, 2, 3, 4, 5, 6]
        maximum_arr = calculate_left_max(6, numbers)
        minimum_arr = calculate_min_right(6, numbers)
        self.assertEqual(find_pivots(6, minimum_arr, maximum_arr, numbers), 6, "Ascending order calculation failed!")   
        
    def test_decreasing_order(self):
        numbers = [6, 5, 4, 3, 2, 1]
        maximum_arr = calculate_left_max(6, numbers)
        minimum_arr = calculate_min_right(6, numbers)
        self.assertEqual(find_pivots(6, minimum_arr, maximum_arr, numbers), 0, "Descending order calculation failed!") 
        
    def test_random_order(self):
        numbers = [1, 2, 5, 15, 9, 11, 4, 17, 12, 6]
        maximum_arr = calculate_left_max(10, numbers)
        minimum_arr = calculate_min_right(10, numbers)
        self.assertEqual(find_pivots(10, minimum_arr, maximum_arr, numbers), 2, "Random order calculation failed!")     
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
