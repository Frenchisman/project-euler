'''

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?

'''


def lcm():
    # We start by computing the factor of all prime numbers < 20, since
    #the number can not be smaller.
    min = 2* 3 * 5 * 7 * 11 * 13 * 17 * 19
    end = False
    while end == False:
        # Check divisibility by all numbers <= 20
        for x in range(2, 21, 1):
            if min % x == 0:
                end = True
            # If not divisible break loop, and check the next number ( +19 for divilibility by 19)
            else:
                end = False
                min += 19
                break
    return min
