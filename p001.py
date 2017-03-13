#!/usr/bin/env python
# Solution to Project Euler problem 1
# Copyright (c) Paulo Vítor. All rights reserved.
#
# https://github.com/PauloFS/ProjectEuler
#

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def compute():
    """ Compute """
    ans = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return str(ans)

if __name__ == "__main__":
    print(compute())
