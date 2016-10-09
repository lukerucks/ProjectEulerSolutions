#Problems 50-60
def factorial(x):
    current = 1
    value = 1
    while current <= x:
        value *= current
        current += 1
    return value


def nCr(n, r):
    value = 1
    current = n
    while current > (n-r):
        value *= current
        current -=1
    value /= factorial(r)
    return value




def problem_53(max_n):
    above_one_million = 0
    for n in range (1, max_n+1):
        r= n/2
        max_value = nCr(n, r)
        while r > 0 and max_value > 1000000:
            if not n%2 and r == n/2:
                above_one_million += 1
            else:
                above_one_million += 2
            r-=1
            if r:
                max_value = nCr(n, r)
    return above_one_million
        

# x = 100
# print problem_53(x)  #Answer: 4075
"""
for n in range(1, x+1):
    for r in range(1, n+1):
        if nCr(n, r) > 1000000:
            print n, r, nCr(n, r)
"""

