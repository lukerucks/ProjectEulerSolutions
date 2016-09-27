def is_palendromic(number):
    s = str(number)
    return s == s[::-1]

def is_Lychrel(number, current_iters, max_iters = 50):
    if current_iters >= max_iters:
        return True
    next_number = number + int(str(number)[::-1])
    if is_palendromic(next_number):
        return False
    return is_Lychrel(next_number, current_iters+1)

def p55():
    lychrel_nums = []
    for i in xrange(10001):
        if is_Lychrel(i, 0):
            lychrel_nums.append(i)
    return lychrel_nums

print len(p55())