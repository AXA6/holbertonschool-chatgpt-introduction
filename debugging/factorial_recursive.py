#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a non-negative integer using recursion.
        Factorial is the product of all positive integers less than or equal to n.
        Example: factorial(4) = 4 * 3 * 2 * 1 = 24

    Parameters:
        n (int): A non-negative integer to compute the factorial for.

    Returns:
        int: The factorial of n. Returns 1 when n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
