'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import sqrt

def sum_primes(n):
    prime_list = []
    for i in range(2, n):
        prime = True
        for p in prime_list:
            if p > sqrt(i):
                break
            if i % p == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(i)
    print(len(prime_list))
    return sum(prime_list)

