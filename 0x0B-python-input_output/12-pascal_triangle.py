#!/usr/bin/python3

'''Task 12 - 12. Pascal's Triangle'''


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n:"""

    if n <= 0:
        return []

    rest = []
    tmp = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(tmp[x] + tmp[x - 1])
            tmp = row
            rest.append(row)
    return rest
