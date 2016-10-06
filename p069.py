from sympy import primefactors, isprime
from itertools import combinations

def find_phi_n(n):
    if isprime(n):
        return n-1
    possible_combinations = primefactors(n)
    total = 0
    add_or_sub = 1
    max_len = len(possible_combinations)
    while possible_combinations:
        new_combinations = []
        for combo in possible_combinations:
            total += n / combo * add_or_sub
        add_or_sub *= -1
        for combo in combinations(possible_combinations, 2):
            if combo[0] * combo[1] < n:
                new_combinations.append(combo[0] * combo[1])
        possible_combinations = new_combinations
    return n-total

#test
def test_relative_primes():
    for i in range(2, 11):
        print i, find_phi_n(i)


def p069():
    current_num = 1
    max_n_over_phi = 0
    max_producing_n = 0
    for prime in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
        current_num *= prime # Will be a combination of the above
        if current_num > 1000000:
            break
        phi = find_phi_n(current_num)
        if float(current_num)/phi > max_n_over_phi:
            max_producing_n = current_num
            max_n_over_phi = float(current_num) / phi
        print current_num, phi, float(current_num)/phi, max_producing_n, max_n_over_phi
    return max_producing_n


print p069()
