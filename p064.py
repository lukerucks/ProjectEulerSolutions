import math
import fractions


def find_fraction_repr(sqroot):
    base = math.sqrt(sqroot)
    a_0 = int(base)
    if base == a_0:
        return int(base)
    all_numbers = [a_0]
    b_1 = a_0
    c_1 = 1
    all_seen_starting_pts = [(0, 1)]
    # format is [(a*sqrt + b) / c]
    a_1, b_1, c_1 = get_next_fraction(sqroot, a_0, 1)
    while (b_1, c_1) not in all_seen_starting_pts:
        all_numbers.append(a_1)
        all_seen_starting_pts.append((b_1, c_1))
        a_1, b_1, c_1 = get_next_fraction(sqroot, b_1, c_1)
    # return [non_repeating, repeating]
    for seen in range(len(all_seen_starting_pts)):
        if all_seen_starting_pts[seen] == (b_1, c_1):
            return (all_numbers[0:seen], all_numbers[seen:])



def get_next_fraction(sq, b,c):
    # comes in as (sqrt - b) / c, where sqrt is the sqrt of sq
    new_c = sq - b**2
    greatest_common_denom = fractions.gcd(new_c, c)
    c /= greatest_common_denom
    new_c /= greatest_common_denom
    max_val = -100
    max_i = 0
    sqrt = math.sqrt(sq)
    for i in range(10):
        val = new_c*i - b
        if val > sqrt:
            break
        elif val > max_val:
            max_val = val
            max_i = i
    # next digit to store, [new_b, new_c]
    return max_i, max_val, new_c


print find_fraction_repr(23)


# Turns out this was unnecessary; from previous attempt
def find_repeating_section(num_list, confirmation_amount=10):
    '''specify as repeating if last section of num_list repeats
    confirmation_amount times'''
    if len(num_list) < confirmation_amount:
        # print 'too short'
        return False
    num_list.reverse()  # So we know we're in repeated section
    hypothesis = []  # Our current belief for what's being repeated
    current_section = []
    count = 0  # Number of successful repeats we've found
    for i in num_list:
        if len(hypothesis) < 2:
            hypothesis.append(i)
            current_section.append(i)
        else:
            if hypothesis == current_section:
                if i == hypothesis[0]:
                    count += 1
                    current_section = []
                    check = [i]
                else:
                    hypothesis.append(i)
                    current_section.append(i)
            elif count >= 1:  # Check to see if we're right
                check.append(i)
                if check != hypothesis[0:len(check)]:  # We're wrong
                    hypothesis += check
                    check = []
                    current_section = [x for x in hypothesis]
                    count = 0
                elif check == hypothesis:  # Another confirmed observation
                    count += 1
                    check = []
        if count >= confirmation_amount:
            break
    if count < confirmation_amount:
        # print "{}<{}".format(count, confirmation_amount)
        num_list.reverse()  # to not alter mutable input list
        return False
    hypothesis.reverse()  # Put back in correct orientation
    possible_orientations = []  # Might not start with right number
    for i in hypothesis:
        possible_orientations.append(hypothesis)
        hypothesis = [hypothesis[-1]] + hypothesis[:-1]

    check = []
    digit = 0
    num_list.reverse()
    while check not in possible_orientations:
        if len(check) == len(hypothesis):
            check.pop(0)
        check.append(num_list[digit])
        digit += 1
    hypothesis = check
    if len(hypothesis) == 2 and hypothesis[0] == hypothesis[1]:
        hypothesis = hypothesis[0]
        digit -= 1
    return (num_list[0:digit-len(hypothesis)], hypothesis)


# print find_repeating_section([1,2,3,1,5,4,5,2,3,1,5,4,5,2,3,1,5,4,5,2,3,1,5,4,5,2], 2)

def p064(total_range):
    odd = 0
    for i in range(1, total_range+1):
        continued_fraction = find_fraction_repr(i)
        if type(continued_fraction) == tuple:
            if len(continued_fraction[1]) % 2:
                odd += 1
        if not i % 100:
            print i
    return odd

print p064(10000)






