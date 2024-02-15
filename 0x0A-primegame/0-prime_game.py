#!/usr/bin/python3
""" 0-prime_game module """


def isWinner(x, nums):
    """prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    get = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not get[i]:
            continue
        for j in range(i * i, n + 1, i):
            get[j] = False
    get[0] = get[1] = False
    c = 0
    for i in range(len(get)):
        if get[i]:
            c += 1
        get[i] = c
    player = 0
    for n in nums:
        player += get[n] % 2 == 1
    if player * 2 == len(nums):
        return None
    if player * 2 > len(nums):
        return "Maria"
    return "Ben"
