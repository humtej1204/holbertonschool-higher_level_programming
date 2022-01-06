#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup_list = my_list.copy()
    for i in range(len(dup_list)):
        dup_list[i] = replace if my_list[i] == search else my_list[i]
    return (dup_list)
