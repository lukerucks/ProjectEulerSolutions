"Project Euler"

"Problem 41"
"""We shall say that an n-digit number is pandigital if it makes use 
of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""







"Problem 43"
"""
The number, 1406357289, is a 0 to 9 pandigital number because 
it is made up of each of the digits 0 to 9 in some order, but it 
also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, 
we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def make_number_from_list(list_of_ints):
    number = 0
    power = 0
    for integer in reversed(list_of_ints):
        number += integer * 10**power
        power += 1
    return number

def problem_43():
    d1_list = [1,2,3,4,5,6,7,8,9] #d1 must not be 0
    d2_list = [0,1,2,3,4,5,6,7,8,9]
    d3_list = [0,1,2,3,4,5,6,7,8,9]
    d4_list = [0,2,4,6,8]  #d2d3d4 must be even
    d5_list = [0,1,2,3,4,5,6,7,8,9] #d3d4d5 must be divisible by 3
    d6_list = [0,5]  #d4d5d6 must be divisible by 5
    d7_list = [0,1,2,3,4,5,6,7,8,9]  #d5d6d7 must be divisible by 7
    d8_list = [0,1,2,3,4,5,6,7,8,9]  #d5d6d7 must be divisible by 11
    d9_list = [0,1,2,3,4,5,6,7,8,9]  #d5d6d7 must be divisible by 13
    d10_list = [0,1,2,3,4,5,6,7,8,9] #d5d6d7 must be divisible by 17
    pandigital_numbers = []
    for d1 in d1_list:
        used = [d1]
        for d2 in d2_list:
            if d2 in used:
                continue
            used = [d1, d2]
            for d3 in d3_list:
                if d3 in used:
                    continue
                used = [d1, d2, d3]
                for d4 in d4_list: #already filtered
                    if d4 in used:
                        continue
                    used = [d1, d2, d3, d4]
                    for d5 in d5_list:
                        d3d4d5 = make_number_from_list([d3,d4,d5])
                        if not d3d4d5 % 3 == 0 or d5 in used:
                            continue
                        used = [d1, d2, d3, d4, d5]
                        for d6 in d6_list: #already filtered
                            if d6 in used:
                                continue
                            used = [d1, d2, d3, d4, d5, d6]
                            for d7 in d7_list:
                                d5d6d7 = make_number_from_list([d5,d6,d7])
                                if not d5d6d7 % 7 == 0 or d7 in used:
                                    continue
                                used = [d1, d2, d3, d4, d5, d6, d7]
                                for d8 in d8_list:
                                    d6d7d8 = make_number_from_list([d6,d7,d8])
                                    if not d6d7d8 % 11 == 0 or d8 in used:
                                        continue
                                    used = [d1, d2, d3, d4, d5, d6, d7, d8]
                                    for d9 in d9_list:
                                        d7d8d9 = make_number_from_list([d7,d8,d9])
                                        if not d7d8d9 % 13 == 0 or d9 in used:
                                            continue
                                        used = [d1, d2, d3, d4, d5, d6, d7, d8, d9]
                                        for d10 in d10_list:
                                            d8d9d10 = make_number_from_list([d8,d9,d10])
                                            if not d8d9d10 % 17 == 0 or d10 in used:
                                                continue
                                            else:
                                                pandigital_numbers.append(make_number_from_list([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]))
    print pandigital_numbers
    #[1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
    pandigital_sum = sum(pandigital_numbers)
    print pandigital_sum
    #16695334890
    return pandigital_sum


#problem_43()

def get_triangular(n):
    return n*(n+1) / 2

def get_pentagonal(n):
    return n*(3*n - 1)/2

def get_hexagonal(n):
    return n*(2*n-1)

def problem_45():
    n = 1
    current_pentagons = []
    current_hexagons = []
    meets_all_three = []
    found = False
    while not found:
        current_pentagons.append(get_pentagonal(n))
        current_hexagons.append(get_hexagonal(n))
        current = get_triangular(n)
        if current in current_pentagons and current in current_hexagons:
            meets_all_three.append(current)
            print current
            if current > 40755:
                found = True
                print "Answer: ", current #1533776805
        n += 1
    print meets_all_three #[1, 40755, 1533776805]
    return current
#problem_45()

import numpy

def find_all_primes_below_n(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]


def find_prime_factors(n, primes):
    factors = {}
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                n /= prime
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
                break
    return factors



def find_consecutive_ints_with_distinct_factors(num_factors, primes):
    current = 1
    found = False
    max_prime = max(primes)
    while not found:
        current += 1
        current_list = []
        current_factors = []
        consecutive = 0
        while consecutive < num_factors:
            number = current + consecutive
            if number in primes:
                found = False
                break
            consecutive += 1
            factors = find_prime_factors(number, primes)
            found = True
            if len(factors) != num_factors:
                found = False
                break
            for each in factors:
                if (each, factors[each]) in current_factors:
                    found = False
                    break
                current_factors.append((each, factors[each]))
            if not found:
                break
        if current > max_prime:
            print "Not enough Primes"
            break
    print "Answer: ", current
    print "Numbers with Factors:"
    for i in range(num_factors):
        number = current + i
        print number, " = ", find_prime_factors(number, primes)
    print current





def problem47():
    primes = find_all_primes_below_n(10000000)
    find_consecutive_ints_with_distinct_factors(4, primes)
    # 134043  =  {3: 1, 491: 1, 13: 1, 7: 1}
    # 134044  =  {47: 1, 2: 2, 31: 1, 23: 1}
    # 134045  =  {17: 1, 83: 1, 19: 1, 5: 1}
    # 134046  =  {11: 1, 2: 1, 3: 2, 677: 1}
    # 134043

def find_Godbach_conjecture_factors(composite, primes):
    for prime in primes:
        if prime > composite:
            return False
        square = 1
        while 2*square**2 + prime < composite:
            square+=1
        if 2*square**2 + prime == composite:
            return prime, square




def problem46():
    primes = find_all_primes_below_n(10000000)
    i = 9
    while True:
        if i not in primes:
            if not find_Godbach_conjecture_factors(i, primes):
                print i
                return i
        i += 2

#problem46()

def get_last_ten_digits(multiplicand1, multiplicand2):
    x = multiplicand1 * multiplicand2
    if len(str(x)) > 10:
        return int(str(x)[-10:])
    else:
        return x

def problem48():
    current = 0
    for i in range(1, 1000):
        current_product = 1
        for j in range(i):
            current_product = get_last_ten_digits(current_product, i)
        current += current_product
        print i, current_product
    current = int(str(current)[-10:])
    print "Answer: ", current
    return current


#problem48()
def is_permutation(n, m):
    n_count = {}
    m_count = {}
    for char in str(n):
        if int(char) not in n_count:
            n_count[int(char)] = 1
        else:
            n_count[int(char)] += 1
    for char in str(m):
        pass



def problem49():
    primes = find_all_primes_below_n(10000)
    









