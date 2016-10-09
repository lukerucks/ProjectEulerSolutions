"Problem 48"
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""




def find_sum_of_series(max_num):
    current = [11, 22]
    while current[-1] < max_num:
        current.append(current[-1] + current[-2])
    print current
    return sum(current)

print 10405071317
print find_sum_of_series(1010)




