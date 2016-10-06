'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from math import sqrt

def nth_prime_slow(n):

    prime_list = [2]
    count = 1
    i = 3
    while count < n:
        prime = True

        for p in prime_list:
            # To determine if a number is prime, we only need to check for
            # factors <= to its square root
            if p > sqrt(i) :
                break
            if i % p == 0:
                prime = False
                break
        # If no divisor < sqrt is found in prime list then the number is 
        # prime. 
        if prime == True:
            prime_list.append(i)
            count += 1

        # We do not need to check even numbers
        i += 2
        
    return prime_list.pop()


