from sympy import primefactors, isprime, primerange
from sympy.ntheory.factor_ import totient
from itertools import combinations
import time


# originally from p069; has occasional off by one error
# replaced by sympy module
def find_phi_n(n):
    if isprime(n):
        return n - 1
    possible_combinations = primefactors(n)
    total = 1
    add_or_sub = 1
    while possible_combinations:
        new_combinations = []
        for combo in possible_combinations:
            total += (n-1) / combo * add_or_sub
        add_or_sub *= -1
        for combo in combinations(possible_combinations, 2):
            if combo[0] * combo[1] < n:
                new_combinations.append(combo[0] * combo[1])
        possible_combinations = new_combinations
    return n-total

def is_permutation(n_1, n_2):
    n_1_list = [x for x in str(n_1)]
    n_2_list = [x for x in str(n_2)]
    return sorted(n_1_list) == sorted(n_2_list)

# time.clock()
# for n in range(10**6, 10**6 + 10):
#     print "For {}, phi is {}, and we've been running for {} seconds.".format(n, find_phi_n(n), time.clock())


def p070(): #too slow for numbers this big
    time.clock()
    min_n_over_phi = 10**7
    min_n = 0
    for n in range(2, 10**5):
        phi = find_phi_n(n)
        if is_permutation(phi, n):
            print "Permutation!  Phi of {} with n of {}".format(phi, n)
            if n/float(phi) < min_n_over_phi:
                min_n = n
                min_n_over_phi = n/float(phi)
                print "Min n set to {} with phi of {}".format(n, phi)
        if  n % 10000 == 0:
            print "{}, min n is {}, with value of {}; it's taken {} s".format(n, min_n, min_n_over_phi, time.clock())
    return min_n, min_n_over_phi



def p070_alternate(power_of_ten):
    time.clock()
    min_n_over_phi = 10**power_of_ten
    min_n = 0
    primes = list(primerange((10**(power_of_ten / 2.0)/3), (10**(power_of_ten / 2.0)*3)))

    for combos in combinations(primes, 2):
        current = combos[0]*combos[1]
        if current <= 10**power_of_ten:
            phi = totient(current)
            if is_permutation(phi, current):
                print "permutation with n={} and phi={}".format(current, phi)
                if current/float(phi) < min_n_over_phi:
                    min_n = current
                    min_n_over_phi = current/float(phi)
                    print "New min!  n={}, phi={}, n/phi={}".format(current, phi, min_n_over_phi)
    return min_n, min_n_over_phi

def test_phi():
    tests = [623452, 12345, 10, 8319823, 24, 260, 5555, 7, 261]
    answers = [311724, 6576, 4, 8313928, 8, 96, 4000, 6, 168]
    correct = 0
    total = 0
    for i in range(len(tests)):
        a = find_phi_n(tests[i])
        if a == answers[i]:
            print "correctly got {} for n of {}".format(a, tests[i])
            correct += 1
        else:
            print "expected {} for n of {}, got {}, a difference of {}".format(answers[i], tests[i], a, a-answers[i])
            print totient(tests[i])
        total += 1
    print "got {} out of {} correct".format(correct, total)




print p070_alternate(7)