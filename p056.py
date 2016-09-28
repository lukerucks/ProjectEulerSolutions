def digital_sum(num):
    total = 0
    for s in str(num):
        total += int(s)
    return total


def p56():
    max_sum = 0
    max_a = 0
    max_b = 0
    for a in range(100):
        for b in range(100):
            x = long(a)**long(b)
            dig_sum = digital_sum(x)
            if dig_sum > max_sum:
                max_sum = dig_sum
                max_a = a
                max_b = b
    print max_a, max_b
    return max_sum

print p56()
