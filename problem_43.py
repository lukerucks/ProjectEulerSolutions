

#Pentagon numbers: 1,5,12,22,35,51,70,92,117,145

# Pk - Pj is pentagonal
# Pk + Pj is pentagonal

# D = abs(Pk - Pj)

# minimum value of D

def find_pentagonal_number(n):
    return n*(3*n-1) / 2

def find_D(P_k, P_j, pentagonal_numbers):
    pentagonal_sum = P_k + P_j
    diff = abs(P_k - P_j)
    if pentagonal_sum in pentagonal_numbers and diff in pentagonal_numbers:
        return diff
    else:
        return None

def get_pentagonal_numbers(max_n):
    pentagonal_numbers = {}
    for n in xrange(1, max_n):
        pentagonal_numbers[find_pentagonal_number(n)] = n
    return pentagonal_numbers

def problem_42():
    pentagonal_numbers = get_pentagonal_numbers(10000)
    min_val = float('inf')
    for P_k in pentagonal_numbers:
        for P_j in pentagonal_numbers:
            if P_k > P_j:
                x = find_D(P_k, P_j, pentagonal_numbers)
                if x is not None and x < min_val:
                    min_val = x
                    print x
    return min_val

problem_42()

