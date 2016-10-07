from fractions import Fraction


def p071():
    result = Fraction('3/7')
    to_subtract = 0
    delta = 0.1**8
    while result == Fraction('3/7'):
        to_subtract += delta
        new_fraction = Fraction('3/7') - Fraction(to_subtract)
        result = new_fraction.limit_denominator(max_denominator=1000000)
    return result


print p071()
