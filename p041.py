import numpy

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

def convert_list_to_int(some_list):
    power_of_ten = len(some_list)-1
    final_int = 0
    for number in some_list:
        final_int += number*10**power_of_ten
        power_of_ten -=1
    return final_int


def find_permutations(current_start, unused, list_of_permutations):
    if not unused:
        list_of_permutations.append(convert_list_to_int(current_start))
    for number in unused:
        to_be_unused = []
        for x in unused:
            if x != number:
                to_be_unused.append(x)
        permutation = find_permutations(current_start + [number], to_be_unused, list_of_permutations)

permutations = []
print "Find pangitital numbers"
digits = [7,6,5,4,3,2,1]  #reversed so 987654321 will be highest
find_permutations([], digits, permutations)

print "Find primes"
primes = find_all_primes_below_n(7654322)

print "Convert to primes dict"
primes_dict = {}
for prime in primes:
    primes_dict[prime] = 1

print "Look for highest prime pan_digital_number"
def problem_41(pan_digital_numbers, primes):
    for pan_digital_number in pan_digital_numbers:
        if pan_digital_number in primes:
            return pan_digital_number

##None was returned for 987654321, and 87654321.
print problem_41(permutations, primes_dict)

