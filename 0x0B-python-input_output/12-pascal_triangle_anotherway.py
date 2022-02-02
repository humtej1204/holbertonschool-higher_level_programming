#!/usr/bin/python3

'''Task 12 - 12. Pascal's Triangle'''


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n:"""
    main_list = []
    if n <= 0:
        return (main_list)
    for y in range(n):
        main_list.append([])
        for x in range(y + 1):
            if x == 0:
                main_list[y].append(1)
            elif x == y:
                main_list[y].append(1)
            else:
                r = main_list[y - 1][x] + main_list[y - 1][x - 1]
                main_list[y].append(r)
    return main_list
