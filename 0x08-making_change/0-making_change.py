#!/usr/bin/python3
""" 0-making_change module
"""


def makeChange(coins, total):
    """ Finds least number of coins needed to make change
    """
    if total < 1:
        return 0

    change_coin_count = 0
    store_value = 0
    coins.sort(reverse=True)

    for coin in coins:
        if not total % coin:
            store_value = total // coin
            break

    for coin in coins:
        if coin < total:
            count = total // coin
            total -= coin * count
            change_coin_count += count

    if total and store_value:
        return store_value
    if not total and change_coin_count > store_value:
        return store_value
    if total and not store_value:
        return -1
    return change_coin_count
