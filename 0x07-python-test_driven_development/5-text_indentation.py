#!/usr/bin/python3

""" Defines a function that prints a text"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: .,? and :

    Args:
        text (str): string to be printed

    Raises:
        TypeError: text must be a string
    """
    for n in range(len(text)):
        if n == 0:
            print(text[n], end='')
            continue
        if text[n - 1] == '.' or text[n - 1] == '?' or text[n - 1] == ':' and text[n] == ' ':
            continue
        print(text[n], end='')
        if test[n] == '.' or text[n] == '?' or text[n] == ':':
            print()
            print()
