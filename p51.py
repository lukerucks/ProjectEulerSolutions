from sympy import sieve, isprime
from itertools import combinations
# from copy import copy, deepcopy


def get_lowest_prime_of_set(n):
    print 'start'
    for prime in sieve:
        str_p = str(prime)
        combos_to_try = get_str_combos(str_p)
        for str_combo in combos_to_try:
            num_primes_in_set = 0
            family = []
            for i in range(10):
                s = str_combo.replace('*', str(i))
                if len(str(int(s))) != len(s):
                    continue
                if isprime(int(s)):
                    num_primes_in_set += 1
                    family.append(int(s))
            if num_primes_in_set >= 7:
                print family
            if num_primes_in_set >= n:
                print "FOUND!"
                return sorted(family)[0]


def get_possible_combinations(r, choose_n):
    '''take in range r, return all combinations of r
    excepting choose 0 or all'''
    if len(r) <= choose_n:
        return tuple([r])
    else:
        combos = []
        choosing = 1
        while choosing <= choose_n:
            for i in range(len(r)):
                r_without_i = r[:i] + r[i + 1:]
                combos += get_possible_combinations(r_without_i, choose_n)
            choosing += 1
        combos = [tuple(x) for x in combos]
        return list(set(combos))


def get_all_combinations(r):
    combos = []
    for i in range(1, len(r)):
        combos += combinations(r, i) #twice as fast as above
    return combos

def get_str_combos(s):
    num_combos = get_all_combinations(range(len(s)))
    str_combos = []
    for num_combo in num_combos:
        current_num = []
        for number in range(len(s)):
            if number in num_combo:
                current_num.append('*')
            else:
                current_num.append(s[number])
        str_combos.append(''.join(current_num))
    return str_combos


print get_lowest_prime_of_set(8)
