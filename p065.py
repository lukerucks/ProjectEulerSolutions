import fractions


def calculate_approx_from_pattern(pattern):
    '''input a list of [a_0, a_1, ... a_n], get approximation'''
    # if len(pattern) == 1:
    #     return pattern[0]
    current = fractions.Fraction(pattern[-1],1)
    for i in range(len(pattern)-2, -1, -1):
        current = fractions.Fraction(pattern[i], 1) + fractions.Fraction(1, current)
    return current

# Test for convergents for sqrt of 2
# print "Test for sqrt(2)"
# pattern = [1]
# for i in range(10):
#     print calculate_approx_from_pattern(pattern)
#     pattern.append(2)


def sum_of_digits_of_numerator(fract):
    return sum([int(x) for x in str(fract.numerator)])


def p065():
    pattern = [2,1,2]
    should_be = [(2,1), (3,1), (8,3), (11,4), (19,7), (87,32), (106,39), (193,71), (1264,465), (1457,536)]
    should_be = [fractions.Fraction(*x) for x in should_be]
    # counter = 0
    for i in range(len(pattern)):
        convergent = calculate_approx_from_pattern(pattern[0:i+1])
        # print convergent, should_be[i], float(convergent), float(should_be[i]), sum_of_digits_of_numerator(convergent)
        # counter += 1
    # counter -= 1
    next_non_one = 4
    while len(pattern) < 100:
        # counter += 1
        if pattern[-1] == pattern[-2] == 1:
            pattern.append(next_non_one)
            next_non_one += 2
        else:
            pattern.append(1)
        if len(pattern) <= 10:
            convergent = calculate_approx_from_pattern(pattern)
            # print counter, convergent, should_be[counter], float(convergent), float(should_be[counter]), pattern, sum_of_digits_of_numerator(convergent)
    convergent = calculate_approx_from_pattern(pattern)
    # print counter, convergent
    return sum_of_digits_of_numerator(convergent)

if __name__ == '__main__':
    print "\ntest for e"
    print p065()
