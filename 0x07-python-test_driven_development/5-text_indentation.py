#!/usr/bin/python3

"""Creting the Function text_indentation"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    i = 0

    if type(text) not in [str]:
        raise TypeError("text must be a string")

    for j in range(len(text)):
        if text[j] == "." or text[j] == "?" or text[j] == ":":
            print(text[i:(j + 1)])
            print("")
            if (j + 1) == len(text):
                continue
            elif text[j + 1] == " ":
                i = j + 2
            else:
                i = j + 1
        else:
            if (j + 1) == len(text):
                print(text[i:], end='')
                break
        j = j + 1
