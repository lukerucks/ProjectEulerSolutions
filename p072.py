from fractions import Fraction
from sympy.ntheory.factor_ import totient

def num_simple_fractions(max_denom):
    '''find number of simple fractions with denominator less than 
    or equal to max_denom)'''
    simple_fractions = set()
    for denom in range(2, max_denom + 1):
        for numerator in range(1, denom):
            s_fraction = Fraction(str(numerator) + '/' + str(denom))
            simple_fractions.add(s_fraction)
    return len(simple_fractions)

# The above is waaaay to slow for this (O(n^2)), but the previous problems
# on relatively prime numbers should be useful, since, if you were creating
# a data structure containing every simple fraction below a number, you would
# only include numerators which were relatively prime as you worked your way
# up denominators


def p072(max_denom):
    total = 0
    for i in range(2, max_denom + 1):
        total += totient(i)
    return total


print p072(1000000)
# 303963552391
# [Finished in 189.0s]