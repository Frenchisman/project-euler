'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

def execute():
    a = 0
    b = 1
    found = False;
    while a < b and found == False:
        # We only need to test for values of a up to 332.
        # Since a < b < c and a + b + c = 1000, 
        # if a > 332 then a + b + c > 1000 
        for a in range(a, 332):
            b = a + 1
            c = 999 - 2 * a
            while b < c:
                result = a * a + b * b
                if(result == c * c):
                    found = True
                    print ('a = '+ str(a) + ', b = ' + str(b) + ', c = ' + str(c) + '\n')
                    print ('a + b + c = '+ str(a+b+c) + '\n')
                    print ('a² + b² = ' + str(a*a+b*b) + '\n')
                    print ('c² = ' + str(c*c) + '\n')
                    break
                b += 1
                c -= 1
            if found == True:
                break
    if found == False:
        print ('Not Found')
        return 0
    return a * b * c

def get_pyth_product(n):
    '''
    Generalization of above function
    '''
    # We can start loop at 1 because if a = 0, then b² = c²,
    # which means sqrt(b) = sqrt(c) 
    # which means either b = c ( impossible ) or b = -c ( also impossible)
    for a in range(1, n//3):
        # a < b so b starts at 2
        for b in range(2, n-a):
            # (a + b + c = n) <=> ( c = n - a - b)
            c = n - a - b
            if a * a + b * b == c * c:
                print ('a = '+ str(a) + ', b = ' + str(b) + ', c = \
' + str(c) + '\n')
                print ('a + b + c = '+ str(a+b+c) + '\n')
                print ('a² + b² = ' + str(a*a+b*b) + '\n')
                print ('c² = ' + str(c*c) + '\n')
                return a * b * c
    print('Not Found')


