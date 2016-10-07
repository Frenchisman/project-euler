'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(sequence, n):
    '''
    Generate the collatz sequence for number n
    Sequence needs to be a list
    '''
    sequence.append(n)
    if n == 1:
        return sequence

    if n % 2 == 0:
        sequence = collatz(sequence, n // 2)
    else:
        sequence = collatz(sequence, 3 * n + 1)

def greatest_collatz(n):
    ''' 
    Find the greatest collatz sequence for starting number <= n
    '''
    greatest_seq = []
    for x in range(n+1):
        seq = []
        seq = collatz(seq, x)
        if len(seq) > len(greatest_seq):
            greatest_seq = seq
    return seq


