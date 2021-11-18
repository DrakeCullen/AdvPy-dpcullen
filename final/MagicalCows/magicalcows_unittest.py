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
    
    def test_no_cows(self):
        max_cows = 5
        cows_per_farm = [0, 0, 0, 0, 0]
        dp = init_dp(max_cows)
        init_farm_counts(dp, cows_per_farm)
        calculate_all_day_counts(dp, max_cows)
        self.assertEqual(check_day(dp, max_cows, 0), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 12), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 19), 0, "No cows are on the farm.")
        self.assertEqual(check_day(dp, max_cows, 50), 0, "No cows are on the farm.")

        
   
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
