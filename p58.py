import sympy
import math


def p58():
    level = 1
    diagonals = [1]
    current = 1
    numerator = 0
    denom = 1
    while float(numerator) / denom >= 0.1 or denom == 1:
        for i in range(4):
            current += 2 * level
            diagonals.append(current)
            if sympy.isprime(current):
                numerator += 1
        denom += 4
        level += 1
        print numerator, '/', denom
    return math.sqrt(current)


# def p58():
#     fraction = 1
#     current_side_length = 0
#     while fraction >= 0.1 or current_side_length < 2:
#         current_side_length += 1
#         diagonals = get_diagonals(current_side_length)
#         num = 0
#         denom = len(diagonals)
#         for x in diagonals:
#             if sympy.isprime(x):
#                 num += 1
#         fraction = float(num) / denom
#     return current_side_length


print p58()
