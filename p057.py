#start with farthest in (2)
#expand out (2+ 1/(n_1))
#when you reach the final stage
# 1+ 1/(n_1)

def expansion(n):
    current = [2,1]
    for i in range(n-1):
        todo = add_fractions([2,1], [current[1], current[0]])
        current = todo
    return add_fractions([1,1], [current[1], current[0]])

#Use Fraction class instead
def add_fractions(a, b):
    '''a and b are both lists of [numerator, denominator]'''
    num = a[0] * b[1] + b[0] * a[1]
    denom = a[1] * b[1]
    return [num, denom]

def simplify_fraction(a):
    num = a[0]
    denom = a[1]
    for i in range(denom, 1, -1):
        if num % i == 0 and denom % i == 0:
            num = num / i
            denom = denom / i
            break
    return [num, denom]

def num_digits(i):
    return len(str(i))

def p57():
    more_in_num = 0
    for i in range(1, 1001):
        exp = simplify_fraction(expansion(i))
        if num_digits(exp[0]) > num_digits(exp[1]):
            more_in_num += 1
    return more_in_num
#print p57()

# Way too slow; simplification is too slow a process by above.  
# Try using built in class
from fractions import Fraction
def f_expansion(n):
    current = Fraction(2,1)
    for i in range(n-1):
        todo = Fraction(2,1) + 1/current
        current = todo
    return 1+1/current

def f_p57():
    more_in_num = 0
    for i in range(1, 1001):
        if i % 10 == 0:
            print i
        num, denom = str(f_expansion(i)).split('/')
        if num_digits(num) > num_digits(denom):
            more_in_num += 1
    return more_in_num

print f_p57()
# num, denom = str(f_expansion(1000)).split('/')
# print num, denom




