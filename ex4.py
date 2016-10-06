'''

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def brute_force_palindrome():
    n_set = set()
    for x in range(100,999):
        for y in range(100,999):
            pal = x * y
            pal = str(pal)
            if pal == pal[::-1] :
                n_set.add(int(pal))
    return max(n_set)