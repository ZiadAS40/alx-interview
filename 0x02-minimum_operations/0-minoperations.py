#!/usr/bin/python3
"""make the min operations function"""


def minOperations(n):
    if n < 2:
        return 0

    def get_primes(n):
        primes = []
        for num in range(2, n):
            is_prime = True
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    primes = get_primes(int(n**0.5))

    def analyze(n, primes):
        result = 0
        for prime in primes:
            division = n / prime
            if division.is_integer() and prime < n:
                result += prime
                result += analyze(int(division), primes)
                return result
        return n

    return analyze(n, primes)
