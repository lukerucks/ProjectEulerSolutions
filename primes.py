import numpy


def find_all_primes_below_n(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p * p // 3:: 2 * p] = False
            prime[p * (p - 2 * (i & 1) + 4) // 3:: 2 * p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2, result]


primes_below_1000000 = find_all_primes_below_n(1000000)
max_prime = primes_below_1000000[-1]

def is_prime(x, primes=primes_below_1000000):



