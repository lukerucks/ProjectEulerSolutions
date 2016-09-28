#Problem 15s
import string
import numpy

def problem_15():
    lattice =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


    current = [0,0]

    """
    start at bottom right
    add 1 for 
    Going only right and down, find how many ways to get
    """

    change = True
    while change:
        change = False
        for x in range(len(lattice)):
            for y in range(len(lattice[0])):
                if lattice[x][y] == 0 and lattice[x+1][y] !=0 and lattice[x][y+1] != 0:
                    lattice[x][y] = lattice[x+1][y] + lattice[x][y+1]
                    change = True

    for each in lattice:
        print each

    print '\n'
    print lattice[0][0]

def problem_20():
    x = long(1)
    for each in range(1,101):
        x*=each
    print x

    x = str(x)
    y = 0
    for each in range(len(x)):
        y += int(x[each])

    print y


def find_devisors_sum(number):
    divisors = []
    for each in range(1, number):
        if number % each == 0:
            divisors.append(each)
    return sum(divisors)


def problem_21():
    divisor_sums = {}
    for each in range(1, 10001):
        divisor_sums[each] = find_devisors_sum(each)
    amicable_numbers = []
    amicable_pairs = []
    for each in divisor_sums:
        if divisor_sums[each] in divisor_sums and divisor_sums[divisor_sums[each]] == each and each != divisor_sums[each]:
            amicable_numbers.append(each)
            amicable_pairs.append((each, divisor_sums[each]))
    print sum(amicable_numbers)
    print amicable_numbers
    print amicable_pairs
    return amicable_numbers

def name_value(name, letter_values):
    name = name.lower()
    letter_score = 0
    for letter in range(len(name)):
        ascii_letter = name[letter]
        if ascii_letter in string.ascii_lowercase:
            letter_score += letter_values[ascii_letter]
    return letter_score



def problem_22(filename):
    letter_values = {
                    'a' : 1,
                    'b' : 2,
                    'c' : 3,
                    'd' : 4,
                    'e' : 5,
                    'f' : 6,
                    'g' : 7,
                    'h' : 8,
                    'i' : 9,
                    'j' : 10,
                    'k' : 11,
                    'l' : 12,
                    'm' : 13,
                    'n' : 14,
                    'o' : 15,
                    'p' : 16,
                    'q' : 17,
                    'r' : 18,
                    's' : 19,
                    't' : 20,
                    'u' : 21,
                    'v' : 22,
                    'w' : 23,
                    'x' : 24,
                    'y' : 25,
                    'z' : 26
                    }
    f = open(filename, 'r')
    names = f.read()
    names = names.split(',')
    names.sort()
    name_total = 0
    for i in range(len(names)):
        name_score = (i+1) * name_value(names[i], letter_values)
        name_total += name_score
    print name_total


#problem_22('p022_names.txt')

def problem_23():
    abundant_numbers = []
    for number in range(1,28123):
        if find_devisors_sum(number) > number:
            abundant_numbers.append(number)
    print "total number of abundant numbers: ", len(abundant_numbers)
    abundant_sums = {}
    for i in abundant_numbers:
        for j in abundant_numbers:
            abundant_sum = i+j
            if abundant_sum not in abundant_sums:
                abundant_sums[abundant_sum] = 1
    total_sum = 0
    for number in range(1,28123):
        if number not in abundant_sums:
            total_sum+=number
    print total_sum
    
def factorial(number):
    product = 1
    for i in range(1, number+1):
        product*=i
    return product

def problem_24_recursive(permutations_left, unknown_digits, known_digits):
    print permutations_left, unknown_digits, known_digits
    if not unknown_digits:
        return known_digits
    if permutations_left <= 0:
        print permutations_left
        return known_digits + unknown_digits
    if permutations_left == 1:
        return known_digits + [unknown_digits[1], unknown_digits[0]]
    if factorial(len(unknown_digits)) < permutations_left:
        print "Problem Here!!!!!"
        return None
    elif factorial(len(unknown_digits)) == permutations_left:
        known_digits += unknown_digits
        return known_digits
    elif factorial(len(unknown_digits)) > permutations_left and permutations_left > factorial(len(unknown_digits)-1):
        current_addition = 0
        current_digit = 0
        while permutations_left - current_addition >= 0:
            print current_digit, permutations_left-current_addition
            current_addition += factorial(len(unknown_digits)-1)
            current_digit +=1
        current_addition -= factorial(len(unknown_digits)-1)
        current_digit -=1
        known_digits.append(unknown_digits[current_digit])
        del unknown_digits[current_digit]
        unknown_digits.sort()
        permutations_left -= current_addition
        
    return problem_24_recursive(permutations_left, unknown_digits, known_digits)


#print problem_24_recursive(999999, [0,1,2,3,4,5,6,7,8,9], [])

def problem_25():
    current_sum = long(0)
    current_term = long(1)
    last_term = long(1)
    term = 1
    while len(str(current_sum)) < 1000:
        current_sum += last_term
        last_term = current_term
        current_term = current_sum
        term += 1
    print term, current_sum



def find_remainder_repetition_length(number, divisor_list, remainder, remainder_dic):
    """ For 1 / number, find the repetion length """

    "First, lets just find the division answer to 20 decimal places"
    if remainder == 0:
        return None
    if not divisor_list:
        x = 10 / number
        divisor_list.append(x)
        remainder = 10 % number
        remainder_dic[remainder] = 1
    else:
        remainder *= 10
        divisor_list.append(remainder / number)
        remainder = remainder % number
        if remainder in remainder_dic:
            return len(remainder_dic)
        else:
            remainder_dic[remainder] = 1
    return find_remainder_repetition_length(number, divisor_list, remainder, remainder_dic)




def problem_26():
    max_len = 0
    max_num = []
    for i in range(2,1000):
        x = find_remainder_repetition_length(i, [], None, {})
        if x > max_len:
            max_num = [i]
            max_len = x
        elif x == max_len:
            max_num.append(i)
    return max_num


            
def find_primes(highest_number, lowest_number, previous_primes = None):
    if previous_primes is None:
        primes = {2:1, 3:1}
    else:
        primes = previous_primes
    counter = 0
    for x in range(lowest_number, highest_number+1):
        will_add = True
        for prime in primes:
            if x % prime == 0:
                will_add = False
                break
        if will_add:
            primes[x] = 1
            counter += 1
            if counter % 5000 == 0:
                print x
    return primes

def find_len_consecutive_primes(primes, highest_number_in_primes, a, b):
    #n**2 + a*n + b
    n = 0
    is_prime = True
    length = 0
    while is_prime:
        x = n**2 + a*n + b
        if x <= highest_number_in_primes:
            if x in primes:
                length +=1
                n+=1
            else:
                return length, highest_number_in_primes
        else:
            lowest = highest_number_in_primes
            highest_number_in_primes += 1000
            primes = find_primes(highest_number_in_primes, lowest, primes)
            print 'Added primes'

def problem_27():
    highest_number_in_primes = 10000
    primes = find_primes(highest_number_in_primes, 2)
    max_len = 0
    max_a = None
    max_b = None
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            length, highest_number_in_primes = find_len_consecutive_primes(primes, highest_number_in_primes, a, b)
            if length > max_len:
                max_len = length
                max_a = a
                max_b = b
    return max_len, max_a, max_b, "Product: ", max_a*max_b
    

def problem_28():
    corners = [1]
    length = 0
    current = 1
    while length < 1000:
        length +=2
        for i in range(4):
            current += length
            corners.append(current)
    return sum(corners)


def problem_29(total_range):
    primes = find_primes(101, 2)
    factors = {}
    for i in range(2, 101):
        if i in primes:
            factors[i] = [i]
            continue
        x = i
        i_factors = []
        while x > 1:
            for prime in primes:
                if x % prime == 0:
                    i_factors.append(prime)
                    x /= prime
        i_factors.sort()
        factors[i] = i_factors
    set_of_combinations = []
    for a in range(2, total_range+1):
        single_instance = [x for x in factors[a]]
        for b in range(2, total_range+1):
            single_instance += factors[a]
            single_instance.sort()
            set_of_combinations.append(tuple(single_instance))
    print len(set_of_combinations)
    set_of_combinations = set(set_of_combinations)
    """
    final_set = []
    for each in set_of_combinations:
        x = 1
        for item in each:
            x *= item
        final_set.append(x)
    final_set.sort()
    print final_set
    """
    print len(set_of_combinations)


def number_is_sum_of_5th_powers_of_digits(number):
    number = str(number)
    digits = []
    for digit in range(len(number)):
        digits.append(int(number[digit])**5)
    return sum(digits) == int(number)


def problem_30():
    sum_list = []
    for i in range(2, 1000000):
        if number_is_sum_of_5th_powers_of_digits(i):
            sum_list.append(i)
    print sum_list
    return sum(sum_list)



def problem_31(current_coins, already_used):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    total = sum(current_coins)
    if total == 200:
        return 1
    else:
        combined = 0
        for each in coins:
            if total + each <= 200:
                new = [x for x in current_coins]
                new.append(each)
                new.sort()
                new.reverse()
                if tuple(new) not in already_used:
                    already_used[tuple(new)] = 1
                    combined += problem_31(new, already_used)
        return combined

#print problem_31([], {})

def is_pandigital_product(a,b):
    """is pandigital if 2 multiplicands and product contain each of 1-9 once."""
    digits_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    product = a*b
    for number in [a,b,product]:
        for letter in str(number):
            if letter == '0':
                return False
            if digits_count[int(letter)] >= 1:
                return False
            else:
                digits_count[int(letter)] = 1
    for digit in digits_count:
        if digits_count[digit] == 0:
            return False
    return True

def problem_32():
    products = {}
    for a in range(2, 5000):
        print a
        for b in range(2, 5000):
            if is_pandigital_product(a, b):
                products[a*b] = 1
    products_sum = 0
    for each in products:
        products_sum += each
    return products_sum


def find_simplified_fraction(numerator, denominator):
    for i in range(numerator+1, 1, -1):
        if denominator % i == 0 and numerator % i == 0:
            denominator /= i
            numerator /= i
            return find_simplified_fraction(numerator, denominator)
    return numerator, denominator

def is_curious_fraction(numerator, denominator):
    if numerator % 10 == 0:
        #trivial case
        return False
    simplifed_numerator, simplifed_denominator = find_simplified_fraction(numerator, denominator)
    for i in (0, 1):
        for j in (0, 1):
            x, y = int(str(numerator)[i]), int(str(denominator)[j])
            u, v = int(str(numerator)[i-1]), int(str(denominator)[j-1])
            if u != v:
                continue
            would_be_numerator, would_be_denominator = find_simplified_fraction(x, y)
            if simplifed_numerator == would_be_numerator and simplifed_denominator == would_be_denominator:
                return True
    return False


def problem_33():
    curious_fractions = []
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if denominator > numerator and is_curious_fraction(numerator, denominator):
                curious_fractions.append((numerator, denominator))
    numerator = 1
    denominator = 1
    for each in curious_fractions:
        numerator *= each[0]
        denominator *= each[1]
    numerator, denominator = find_simplified_fraction(numerator, denominator)
    return denominator

def is_sum_of_digit_factorials(number):
    total_sum = 0
    for digit in str(number):
        total_sum += factorial(int(digit))
    return total_sum == number

def problem_34():
    curious_numbers = []
    for number in range(10, 1000000):
        if is_sum_of_digit_factorials(number):
            curious_numbers.append(number)
    print curious_numbers
    return sum(curious_numbers)

def find_other_elements_left(element_list, full_list):
    elements_left = [x for x in element_list]
    return_list = [x for x in full_list]
    while elements_left:
        for each in range(len(return_list)):
            if return_list[each] in elements_left:
                for item in range(len(elements_left)):
                    if return_list[each] == elements_left[item]:
                        del elements_left[item]
                        del return_list[each]
                        break
                break
    return_list.sort()
    return return_list


def find_permutations_of_number(number):
    permutations = []
    digits = [int(x) for x in str(number)]
    todo = [tuple([x]) for x in digits]
    searched = []
    complete = []
    while todo:
        current = todo.pop(0)
        if tuple(current) not in searched:
            searched.append(tuple(current))
        left_over_list = find_other_elements_left(list(current), digits)
        if left_over_list:
            for each in left_over_list:
                x = tuple(list(current) + [each])
                if x not in searched:
                    todo.append(x)
        else:
            if tuple(current) not in complete:
                complete.append(tuple(current))
    final = []
    for each in complete:
        number = ""
        for digit in each:
            number += str(digit)
        number = int(number)
        final.append(number)
    return final

def find_rotations_of_number(number):
    rotations = []
    digits = [x for x in str(number)]
    for each in range(len(digits)):
        first_half = digits[each:]
        last_half = digits[:each]
        new_rotation = first_half + last_half
        new_number = ""
        for digit in new_rotation:
            new_number += digit
        rotations.append(int(new_number))
    return rotations

def problem_35():
    primes = find_primes(1000000, 2)
    print 'found primes'
    circular_primes = []
    counter = 9
    for prime in primes:
        counter += 1
        if counter % 1000 == 0:
            print "Counter: ", counter
        #permuations = find_permutations_of_number(prime)  #Not what the problem is asking for....
        rotations = find_rotations_of_number(prime)
        can_add = True
        for each in rotations:
            if each not in primes:
                can_add = False
                break
        if can_add:
            circular_primes.append(prime)
            print prime
    return len(circular_primes)

def is_binary_palendrome(number):
    binary_string = "{0:b}".format(number)
    return binary_string == binary_string[::-1]

def problem_36():
    palendrome_numbers = []
    for number in range(1, 1000000):
        if str(number) == str(number)[::-1] and is_binary_palendrome(number):
            palendrome_numbers.append(number)
    return sum(palendrome_numbers)


def is_truncatable_prime(number, primes):
    if int(str(number)[0]) not in primes:
        return False
    if int(str(number)[-1]) not in primes:
        return False
    if len(str(number)) < 2:
        return False
    for digit in range(len(str(number))-1):
        if int(str(number)[:-(digit+1)]) not in primes:
            return False
        if int(str(number)[digit:]) not in primes:
            return False
    return True

def problem_37():
    primes = find_primes(1000000, 2)
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime, primes):
            truncatable_primes.append(prime)
    truncatable_primes.sort()
    print truncatable_primes
    print "length = ", len(truncatable_primes)
    return sum(truncatable_primes)

def is_pandigital_multiple(number):
    products = []
    for n in range(1, 10):
        products.append(number*n)
    str_concatination = ""
    n = 0
    while len(str_concatination) < 9:
        str_concatination += str(products[n])
        n+=1
    digits_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for letter in str_concatination:
        if letter == '0':
            return False
        if digits_count[int(letter)] >= 1:
            return False
        else:
            digits_count[int(letter)] = 1
    for digit in digits_count:
        if digits_count[digit] == 0:
            return False
    return str_concatination


def problem_38():
    max_pandigital = 0
    for number in range(1,100000000):
        if number % 10000 == 0:
            print number
        x = is_pandigital_multiple(number)
        if x and x > max_pandigital:
            max_pandigital = x
    return max_pandigital


def problem_39():
    perimiters = {}
    for k in range(1, 100):
        for m in range(2, 500):
            for n in range(1, 300):
                if m > n:
                    a = k*(m**2 - n**2)
                    b = k*(2*m*n)
                    c = k*(m**2 + n**2)
                    p = a+b+c
                    if p < 1000:
                        if p not in perimiters:
                            perimiters[p] = [(a,b,c)]
                        elif (a,b,c) not in perimiters[p]:
                            perimiters[p].append((a,b,c))
    max_perimiter = 0
    max_solutions = 0
    for p in perimiters:
        if len(perimiters[p]) > max_solutions:
            max_perimiter = p
            max_solutions = len(perimiters[p])
    print max_perimiter, " : ", max_solutions
    return max_perimiter

def problem_40():
    power = 0
    digit = 0
    current_number = 0
    d_n_list = []
    while power < 7:
        if digit + len(str(current_number+1)) >= 10 ** power:
            to_go = (10 ** power) - digit
            d_n_list.append(str(current_number+1)[to_go-1])
            power+=1
        current_number +=1
        digit += len(str(current_number))
    print d_n_list
    product = 1
    for each in d_n_list:
        product *= int(each)
    return product


def sieve_of_eratosthenes_dict(highest_number):
    A = [True for x in range(2, highest_number+1)]
    for i in range(2, int(highest_number**0.5)):
        if A[i]:
            j = i**2
            while j < n:
                A[j] = False
                j += i
    primes = {}
    for each in range(len(A)):
        if A[each]:
            primes[each] = 1
    return primes

def sieve_of_eratosthenes_list(highest_number):
    A = [True for x in range(2, highest_number+1)]
    for i in range(2, int(highest_number**0.5)):
        if A[i]:
            j = i**2
            while j < n:
                A[j] = False
                j += i
    primes = []
    for each in range(len(A)):
        if A[each]:
            primes.append(2+each)
    return primes

def find_all_primes_below_n(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]

def is_pandigital_number(number):
    digits_count = {}
    for i in range(1, len(str(number))):
        digits_count[i] = 0
    for letter in str(number):
        if int(letter) not in digits_count:
            return False
        if digits_count[int(letter)] >= 1:
            return False
        else:
            digits_count[int(letter)] = 1
    for digit in digits_count:
        if digits_count[digit] == 0:
            return False
    return True

def problem_41():
    primes = find_all_primes_below_n(987654)
    print "Found primes"
    for prime in range(len(primes)-1, 0, -1):
        if is_pandigital_number(primes[prime]):
            return primes[prime]













        



    














        













