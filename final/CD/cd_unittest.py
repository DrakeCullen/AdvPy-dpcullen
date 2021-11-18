#!/usr/bin/env python3
import unittest
from cd import calculate_current_test

class CDTest(unittest.TestCase):        
    def test_two_empty_lists(self):
        jack_list = []
        jill_list = []
        self.assertEqual(calculate_current_test(0, 0, jack_list, jill_list), 0, "Neither one owns a CD!")
        
    def test_one_empty_list(self):
        jack_list = [2]
        jill_list = []
        self.assertEqual(calculate_current_test(1, 0, jack_list, jill_list), 0, "Jill doesn't own a CD!")
        
    def test_same_single_cd(self):
        jack_list = [2]
        jill_list = [2]
        self.assertEqual(calculate_current_test(1, 1, jack_list, jill_list), 1, "They have one of the same CD!") 
    
    def test_no_common_cds(self):
        jack_list = [1, 2, 1239, 3848, 9130, 24981]
        jill_list = [7, 92, 281, 833, 3249]
        self.assertEqual(calculate_current_test(5, 4, jack_list, jill_list), 0, "They have none of the same CDs!")
        
    def test_subset_of_cds(self):
        jack_list = [2, 7, 92, 9130, 24981, 294293]
        jill_list = [7, 81, 92, 833, 24981, 92394]
        self.assertEqual(calculate_current_test(5, 5, jack_list, jill_list), 3, "They have 3 CDs in common!")
   
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
