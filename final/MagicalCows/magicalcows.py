#!/usr/bin/env python3
import sys

def get_metrics():
    c, n, m = sys.stdin.readline().split()
    return int(c), int(n), int(m) 

def init_dp(max_cows):
    dp = [x[:] for x in [[1] * (max_cows + 1)] * 51]
    for i in range(51):
        for j in range(max_cows + 1):
            dp[i][j] = 0
    return dp

def read_cows_on_farms(number_farms):
    cows_per_farm = []
    for i in range(number_farms):
        cow = int(sys.stdin.readline())
        cows_per_farm.append(cow)
    return cows_per_farm

def init_farm_counts(dp, cows_per_farm):
    for cow in cows_per_farm:
        dp[0][cow] += 1
        
def calculate_all_day_counts(dp, max_cows):
    for i in range(50):
        for j in range(1, max_cows + 1):
            if (j <= max_cows //2):
                dp[i+1][j*2] += dp[i][j];
            else:
                dp[i+1][j] += 2*dp[i][j];

def check_day(dp, max_cows, day):
    tot = 0;
    for i in range(max_cows + 1):
        tot += dp[day][i];
    return tot

def print_inspection_day_values(dp, checkin_days, max_cows):
    for day in checkin_days:
        tot = check_day(dp, max_cows, day)
        sys.stdout.write(str(tot) + '\n')
      
def main():
    max_cows, number_farms, days = get_metrics()
    dp = init_dp(max_cows)
    cows_per_farm = read_cows_on_farms(number_farms)
    init_farm_counts(dp, cows_per_farm)
    checkin_days = list(map(int, sys.stdin.readlines()))
    calculate_all_day_counts(dp, max_cows)
    print_inspection_day_values(dp, checkin_days, max_cows)
    
if __name__ == "__main__":
    main()