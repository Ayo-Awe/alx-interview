#!/usr/bin/python3

"""This module contains code for the
prime game alx interview question
"""


def isWinner(x, nums):
    """returns the name of the player
    with the most wins
    """

    maria_points = 0
    ben_points = 0

    for i in range(x):
        no_primes = no_primes_in_range(nums[i])
        is_even = no_primes % 2 == 0

        if is_even:
            # Ben wins
            ben_points += 1
        else:
            # Maria wins
            maria_points += 1

    if ben_points == maria_points:
        return None

    return "Ben" if ben_points > maria_points else "Maria"


def no_primes_in_range(end):
    """returns the number of prime numbers
    from 1 to the end number(inclusive)
    """

    if end <= 1:
        return 0

    nums_in_range = range(2, end+1)

    primes_in_range = []

    for num in nums_in_range:
        if is_prime(num, primes_in_range):
            primes_in_range.append(num)

    return len(primes_in_range)


def is_prime(num, preceding_primes):
    """checks if a number is a prime number
    by checking if it's divisible by any prime number
    that comes before it
    """

    for prime in preceding_primes:
        if num % prime == 0:
            return False

    return True
