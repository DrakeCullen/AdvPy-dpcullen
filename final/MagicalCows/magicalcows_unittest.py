#!/usr/bin/env python3
import unittest
from magicalcows import init_dp, init_farm_counts, calculate_all_day_counts, check_day

class MagicalCowsTest(unittest.TestCase):        
    def test_init_dp(self):
        max_cows = 5
        dp = init_dp(max_cows)
        self.assertEqual(dp[0][0], 0, "All values should be initialized to 0.")
        self.assertEqual(dp[0][4], 0, "All values should be initialized to 0.")
        self.assertEqual(dp[3][1], 0, "All values should be initialized to 0.")
        self.assertEqual(dp[19][2], 0, "All values should be initialized to 0.")
        self.assertEqual(dp[50][0], 0, "All values should be initialized to 0.")
    
    def test_no_cows(self):
        max_cows = 5
        dp = init_dp(max_cows)
        calculate_all_day_counts(dp, max_cows)
        self.assertEqual(check_day(dp, max_cows, 0), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 12), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 19), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 50), 0, "No cows are on the farm.")
    
    def test_initial_one_cow(self):
        max_cows = 1
        cows_per_farm = [1]
        dp = init_dp(max_cows)
        init_farm_counts(dp, cows_per_farm)
        calculate_all_day_counts(dp, max_cows)
        self.assertEqual(check_day(dp, max_cows, 0), 1, "There is initially 1 cow.")
        self.assertEqual(check_day(dp, max_cows, 12), 4096, "There are 2^12 cows.")
        self.assertEqual(check_day(dp, max_cows, 19), 524288, "There are 2^19 cows.")
        self.assertEqual(check_day(dp, max_cows, 50), 1125899906842624, "There are 2^50 cows.")
        
    
    def test_initial_many_cows(self):
        max_cows = 5
        cows_per_farm = [1, 2, 4, 1, 4]
        dp = init_dp(max_cows)
        init_farm_counts(dp, cows_per_farm)
        calculate_all_day_counts(dp, max_cows)
        self.assertEqual(check_day(dp, max_cows, 0), 5, "There is initially 5 cows.")
        self.assertEqual(check_day(dp, max_cows, 1), 7, "There are 7 cows on the second day")
   
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
