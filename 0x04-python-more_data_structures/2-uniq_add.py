#!/usr/bin/python3
def uniq_add(my_list=[]):
    sm = 0
    list_uq = list(dict.fromkeys(my_list))
    for i in range(len(list_uq)):
        sm += list_uq[i]
    return (sm)
