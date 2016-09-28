

def find_limit():
    power = 1
    while power == len(str(9**power)):
        power += 1
    power -= 1
    print power
    print 9**power
    print len(str(9**power))


# find_limit()
# limit is 9**21, or 109418989131512359209

def p063():
    totals = []
    for base in range(1, 10):
        for power in range(1, 22):
            if power == len(str(base**power)):
                totals.append((base, power))
    return len(totals), totals

print p063()
