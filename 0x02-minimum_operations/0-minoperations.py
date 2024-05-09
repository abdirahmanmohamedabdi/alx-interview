#!/usr/bin/python3
"""
Main file for """


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
