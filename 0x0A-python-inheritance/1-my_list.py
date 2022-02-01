#!/usr/bin/python3

'''Task 01 - 1. My list'''


class MyList(list):
    '''class MyList'''
    def print_sorted(self):
        '''Function that prints the list,
        but sorted (ascending sort)'''
        print(sorted(self))
