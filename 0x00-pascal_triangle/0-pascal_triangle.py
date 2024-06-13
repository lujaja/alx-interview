#!/usr/bin/python3
"""
Function that returns a list of lists of integers
 representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Function prototype
    Args:
        n which is an integer
    """
    if (n <= 0):
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        curr = [1]
        for i in range(len(prev) - 1):
            curr.append(prev[i] + prev[i + 1])
        curr.append(1)
        triangle.append(curr)
    return triangle
