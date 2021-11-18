#!/usr/bin/env python3
import sys

def get_jack_and_jill_count():
    n, k = sys.stdin.readline().split()
    return int(n), int(k) 


def read_jack_and_jill(jack_count, jill_count, jack_list, jill_list):
    for i in range(jack_count):
        jack_list[i] = int(sys.stdin.readline());
    for i in range(jill_count):
        jill_list[i] = int(sys.stdin.readline());


def calculate_current_test(jack_count, jill_count, jack_list, jill_list):
    i1 = 0
    i2 = 0
    ans = 0
    while i1 < jack_count and i2 < jill_count:
            if jack_list[i1] < jill_list[i2]:
                while jack_list[i1] < jill_list[i2] and i1 < jack_count:
                    i1 += 1
            elif jack_list[i1] > jill_list[i2]:
                while jack_list[i1] > jill_list[i2] and i2 < jill_count:
                    i2 += 1
            else:
                i1 += 1
                i2 += 1
                ans += 1
    return ans

def main_loop(jack_count, jill_count):
    jack_list = [0] * 1000002
    jill_list = [0] * 1000002
    
    while jack_count != 0 or jill_count != 0:
        read_jack_and_jill(jack_count, jill_count, jack_list, jill_list)
        ans = calculate_current_test(jack_count, jill_count, jack_list, jill_list)
        sys.stdout.write(str(ans) + '\n')
        jack_count, jill_count = get_jack_and_jill_count()
        
def main():
    jack_count, jill_count = get_jack_and_jill_count()
    main_loop(jack_count, jill_count)
    
if __name__ == "__main__":
    main()