from sympy import sieve, isprime
from heapq import heappush, heappop
import time

# Starting 2 primes with value to add on, use heap with 
# lowest minimum value with additional prime added as priority
# add primes and prime sets to the heap as priority goes up
# with each set taken off the heap, start with the minimum prime
# that can be added to it based off of its current priority.
# if it can be added, add it to the heap with the relevant priority
# keep on the same set until you reach the next minimum priority 
# *before* you started this set.  After this has been reached, add the set
# back to the heap with a priority one greater than the last priority 
# which could have been checked.


def p60(max_level):
    """Should work for all cases where the minimum value in the set is below
    the latter number in the first primerange, 10000 in this instance
    """
    clock = time.clock()
    new_sets = []
    # start with heap of primes for efficiency
    for prime in sieve.primerange(3, 10000):
        # heap: (priority, next_prime_to_check, set)
        priority = prime * max_level + sum(range(1, max_level))
        heappush(new_sets, (priority, prime+1, [prime]))
    while new_sets:
        current_priority, start_prime, current_set = heappop(new_sets)
        levels_left = max_level - len(current_set)
        final_priority = new_sets[0][0]
        if len(current_set) == max_level:
            return current_set, sum(current_set)
        max_prime = (final_priority - sum(current_set) - sum(range(levels_left)))/levels_left
        for prime in sieve.primerange(start_prime, max_prime + 1):
            possible_set = current_set + [prime]
            if evaluate_set(possible_set):
                new_priority = sum(possible_set) + sum(range(prime + 1, prime + levels_left))
                heappush(new_sets, (new_priority, prime + 1, possible_set))
                if len(possible_set) >= 4:
                    print "Added {} with priority {}; {:.2f} seconds have elapsed.".format(possible_set, 
                                                                                        new_priority, time.clock())
        new_priority = sum(current_set) + sum(range(max_prime + 1, max_prime + levels_left + 1))
        heappush(new_sets, (new_priority, max_prime + 1, current_set))


def evaluate_set(primes):
    '''evaluate prime set to see if each combination pair can form 
    new primes in either direction of concatenation'''
    for prime in primes:
        for other_prime in primes:
            if prime != other_prime:
                new = int(str(prime) + str(other_prime))
                if not isprime(new):
                    return False
    return True

# print p60(5)

# Results:
# Added [3, 7, 109, 673] with priority 1466; 1.75 seconds have elapsed.
# Added [23, 311, 677, 827] with priority 2666; 5.96 seconds have elapsed.
# Added [11, 23, 743, 1871] with priority 4520; 23.63 seconds have elapsed.
# Added [3, 17, 449, 2069] with priority 4608; 25.04 seconds have elapsed.
# Added [3, 37, 67, 2377] with priority 4862; 29.31 seconds have elapsed.
#  ... / ... / ...
# Added [37, 1873, 7963, 8011] with priority 25896; 5095.55 seconds have elapsed.
# Added [1847, 2687, 4007, 8693] with priority 25928; 5111.09 seconds have elapsed.
# Added [1783, 2953, 4273, 8461] with priority 25932; 5112.80 seconds have elapsed.
# Added [311, 1223, 6761, 8867] with priority 26030; 5160.28 seconds have elapsed.
# Added [13, 5197, 5701, 6733, 8389] with priority 26033; 5161.72 seconds have elapsed.
# ([13, 5197, 5701, 6733, 8389], 26033)
# [Finished in 11038.4s]


def p060_alternate(num_sets, max_value = 10000):
    '''this only works if you can guarantee the 
    maximum prime in your final set is below max_value'''
    sets = []
    solutions_sets = []
    level = 1
    for prime in sieve.primerange(3, max_value):
        for other_prime in sieve.primerange(prime + 1, max_value):
            possible_set = [prime, other_prime]
            if evaluate_set(possible_set):
                sets.append(possible_set)
    print 'done with sets of 2'
    while sets:
        next_set = sets.pop(0)
        if len(next_set) > level:
            level = len(next_set)
            print "starting level {}, which contains {} sets".format(level, len(sets))
        for prime in sieve.primerange(next_set[-1] + 1, max_value):
            possible_set = next_set + [prime]
            if evaluate_set(possible_set):
                if len(possible_set) == num_sets:
                    solutions_sets.append(possible_set)
                else:
                    sets.append(possible_set)
    min_set = solutions_sets[0]
    min_sum = sum(solutions_sets[0])
    print solutions_sets
    for s in solutions_sets:
        if sum(s) < min_sum:
            min_set = s
            min_sum = sum(s)
    return sum(s), min_set


print p060_alternate(5)

# Still slow, but works faster.  Results:
# starting level 2, which contains 18175 sets
# starting level 3, which contains 9903 sets
# starting level 4, which contains 293 sets
# [[13, 5197, 5701, 6733, 8389]]
# (26033, [13, 5197, 5701, 6733, 8389])
# [Finished in 671.5s]

