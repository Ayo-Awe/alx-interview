#!/usr/bin/python3
"""This module contais code for the making change
alx interview task
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Returns the least amount of coins required
    to makeup total
    """

    if total <= 0:
        return 0

    sorted_coins = sorted(coins[:], reverse=True)

    min = sorted_coins[-1]

    if (min > total):
        return -1

    total_coins = 0
    remainder = total

    for coin in sorted_coins:
        num_coins = remainder//coin
        total_coins += num_coins
        remainder -= num_coins * coin

        if remainder == 0:
            break

    if remainder != 0:
        return -1

    return total_coins
