#!/usr/bin/python3

'''Task 12 - 12. Pascal's Triangle'''


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n:"""

    t_pascal = list()
    if n <= 0:
        return (t_pascal)

    for i in range(1, n + 1):
        t_pascal.append([1 for j in range(i)])

    for i in range(2, len(t_pascal)):
        prev_list = t_pascal[i - 1]
        curr_list = t_pascal[i]
        for j in range(len(prev_list) - 1):
            curr_list[j + 1] = prev_list[j] + prev_list[j + 1]

    return (t_pascal)
