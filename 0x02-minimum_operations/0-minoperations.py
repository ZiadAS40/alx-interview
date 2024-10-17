#!/usr/bin/python3
"""make the min operations function"""


def minOperations(n):
    """
    finding the minimum number of opertions in a file
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:

        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
    