#!/usr/bin/python3
"""
this module defines the Pascal's Triangle function
"""


def pascal_triangle(n):
    """
    this stands for the size(n) of pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        th_triangle = triangle[-1]
        new = [1]
        for d in range(len(th_triangle) - 1):
            new.append(th_triangle[d] + th_triangle[d + 1])
        new.append(1)
        triangle.append(new)
    return (triangle)
