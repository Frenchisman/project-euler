'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt


def get_prime_factors(n):
    '''
    Return a list of n's prime factors
    '''

    i = 2
    prime_factors = []
    max_prime = sqrt(n)
    while i <= max_prime:
        if n % i == 0:
            prime_factors.append(i)
            n = n / i
            max_prime = sqrt(n)
        i += 1

    return prime_factors


def get_max_prime_factor(n):
    prime_factors = get_prime_factors(n)
    print 'Prime Factors : ' + str(prime_factors)
    print 'Max Prime Factor : ' + str(max(prime_factors))
    return max(prime_factors)
