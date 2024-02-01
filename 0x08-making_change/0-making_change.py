#!/usr/bin/python3
""" 0-making_change module
"""


def makeChange(coins, total):
    """ Finds least number of coins needed to make change
    """
    if total < 1:
        return 0

    change_coin_count = 0
    coins.sort(reverse=True)

    for coin in coins:
        if coin < total:
            count = total // coin
            total -= coin * count
            change_coin_count += count
    return change_coin_count if not total else -1
