def problem_1(start, finish):
    current = 0
    for number in xrange(start, finish):
        if number % 3 == 0 or number % 5 == 0:
            #print number
            current += number
    return current

#print problem_1(3, 1000)








def problem_2(highest_term):
    current = 2
    last = 1
    even_sum = 2
    while current < highest_term:
        next = current+last
        last = current
        current = next
        last_digit = str(current)[-1]
        evens = [0,2,4,6,8]
        if int(last_digit) in evens:
            even_sum += current
    return even_sum

print problem_2(4000000)