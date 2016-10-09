from math import factorial


def find_chain(n):
    '''return non-repeating chain of numbers computed from
    factorials of the digits of the previous number'''
    seen = []
    while n not in seen:
        seen.append(n)
        n = sum([factorial(int(x)) for x in str(n)])  # get factorial of digits
    return seen


def p074():
    total = 0
    for i in range(1, 1000000):
        chain = find_chain(i)
        if len(chain) == 60:
            total += 1
    return total


# print p074()
# 402
# [Finished in 200.6s]
