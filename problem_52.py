# problem 52 Project Euler
# Solution by Luke Rucks

# Permuted Multiples
# It can be seen that the number, 125874, 
# and its double, 251748, contain exactly the same digits, 
# but in a different order.

# Find the smallest positive integer, x, such that 2x, 
# 3x, 4x, 5x, and 6x, contain the same digits.

def contains_same_digits(x, y, x_sorted = None):
    if not x_sorted:
        x = sorted([int(i) for i in str(x)])
    else:
        x = x_sorted
    y = sorted([int(j) for j in str(y)])
    return  x == y

# tests = [(1234, 1234),
#         (1234, 4321),
#         (1234554321, 5432112345),
#         (123, 1234),
#         (0, 1)]

# for test in tests:
#     print contains_same_digits(*test)

def number_fits(x):
    if contains_same_digits(x, 2*x):
        x_sorted = sorted([int(i) for i in str(x)])
        for i in range(3, 7):
            if not contains_same_digits(x, i*x, x_sorted):
                return False
            if i == 6:
                return True
    return False

x = 1
while not number_fits(x):
    x += 1

print x
