#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    new_list = list(my_list)
    for i in range(len(my_list)):
        if idx != i:
            new_list[i] = my_list[i]
        else:
            new_list[i] = element
    return new_list
