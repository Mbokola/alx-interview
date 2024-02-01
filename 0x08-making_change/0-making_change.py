#!/usr/bin/python3
""" 0-making_change module
"""


def makeChange(coins, total):
    """ Finds least number of coins needed to make change
    """
    if total < 1:
        return 0

    change_coin_count = 0

    while (total):
        coins.sort(reverse=True)
        for coin in coins:
            if coin <= total:
                count = total // coin
                total -= coin * count
                change_coin_count += count
        if not coins:
            return -1

        if total:
            coins.sort()
            coins.pop()

    return change_coin_count
