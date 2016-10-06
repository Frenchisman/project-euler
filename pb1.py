'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
import time


def compare_times(range):
    '''
    Function to call to get results and exectution times for the functions.

    '''
    test_method(basic_sum, range)
    test_method(custom_counters, range)
    test_method(so1, range)
    test_method(so2_generator_expression, range)
    test_method(so3_sets_generator, range)


def test_method(method, range):

    print('Execution for ' + method.__name__ + ' :')
    # Init variables
    total_time = 0
    fastest = 0
    slowest = 0
    this_time = None

    # Run functions 2k times to eliminate variance
    for x in xrange(1, 2000):

        start = time.clock()
        res = method(range)
        end = time.clock()
        this_time = (end - start)
        total_time += this_time

        if x == 1:
            fastest = this_time
            slowest = this_time
        else:

            if this_time > slowest:
                slowest = this_time

            if this_time < fastest:
                fastest = this_time

    mean_time = total_time / 10

    print('Result : ' + str(res) + ' Mean Time : ' + str(mean_time) +
          ' Fastest : ' + str(fastest) + ' Slowest : ' + str(slowest) + '\n')


def basic_sum(range):
    '''

    Basic Iteration of the loop. Count from 1 to 5000, check if current number
    is divisible by 3 or 5 and add it.

    '''
    sum = 0
    for x in xrange(1, range):
        if x % 3 == 0 or x % 5 == 0:
            sum += x

    return sum


def custom_counters(range):
    '''
    Custom counter iteration to only get multiples of 3 and 5,
    add them to a set and then sum them.

    '''
    num_set = set()
    i = 3
    while i < range:
        num_set.add(i)
        i += 3

    i = 5
    while i < range:
        num_set.add(i)
        i += 5

    return sum(num_set)


def so1(range):
    return sum([i for i in xrange(range) if i % 3 == 0 or i % 5 == 0])


def so2_generator_expression(range):
    return sum(i for i in xrange(range) if i % 3 == 0 or i % 5 == 0)


def so3_sets_generator(range):
    return sum(set(list(xrange(0, range, 3)) + list(xrange(0, range, 5))))
