import math
import time
from p064 import find_fraction_repr
from p065 import calculate_approx_from_pattern


def get_quad_Dioph_using_continued_fractions(D):
    sqrt_n = math.sqrt(D)
    if int(sqrt_n) == sqrt_n:
        return None, None
    continued_fraction = find_fraction_repr(D)
    print continued_fraction
    pattern = continued_fraction[0]
    current_len = 1
    while current_len <= len(pattern):
        fract = calculate_approx_from_pattern(pattern)
        x, y = fract.numerator, fract.denominator
        if (x**2 - D*y**2) == 1:
            return x, y
        current_len += 1
    current_len = 0
    while True:
        next_number = continued_fraction[1][current_len % len(continued_fraction[1])]
        pattern.append(next_number)
        if not next_number:
            continue
        fract = calculate_approx_from_pattern(pattern)
        x, y = fract.numerator, fract.denominator
        if (x**2 - D*y**2) == 1:
            return x, y
        current_len += 1


time.clock()
max_x = 0
max_D = None
for D in range(2, 1000):
    x, y = get_quad_Dioph_using_continued_fractions(D)
    if x and x > max_x:
        max_x = x
        max_D = D
    # print "D: {}, x:{}, y:{}, max_x:{}, max_D:{}, time elapsed:{} s".format(D, x, y, max_x, max_D, time.clock())
print max_x, max_D


# Original without knowing pell's equation solution; very slow
def get_quadratic_Diophantine(D):
    sqrt_n = math.sqrt(D)
    if int(sqrt_n) == sqrt_n:
        return None, None
    found = False
    y = 0
    while True: 
        y += 1
        x = math.sqrt(1 + y**2 * D)
        if (int(x)**2 - D*y**2) == 1:
            return int(x), y