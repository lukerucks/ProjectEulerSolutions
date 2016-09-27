
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
    print "Found Primes!"
    return primes


def get_digits_in_number(number):
    digits = {}
    for char in str(number):
        if char not in digits:
            digits[char] = 1
        else:
            digits[char] += 1
    return digits


def problem_49(primes):
    sequences = []
    for increment_amount in range(1, 5000):
        for first_number in range(1000, 9999):
            found = True
            sequence = [first_number, first_number + increment_amount, first_number + 2 * increment_amount]
            current_digits = {}
            for number in sequence:
                if number not in primes:
                    found = False
                    break
                if not current_digits:
                    current_digits = get_digits_in_number(number)
                elif current_digits != get_digits_in_number(number):
                    found = False
                    break
            if found:
                sequences.append(sequence)
    return sequences

print problem_49(find_primes(10000, 2))
            


