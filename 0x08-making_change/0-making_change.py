#!/usr/bin/python3
""" 0-making_change module
"""


def makeChange(coins, total):
    """ Finds least number of coins needed to make change
    """
    change_coin_count = 0
    coins.sort(reverse=True)

    while (total > 0 and coins):
        for coin in coins:
            if coin <= total:
                count = total // coin
                total -= coin * count
                change_coin_count += count
        if total:
            del coins[0]

    return change_coin_count if not total else -1
