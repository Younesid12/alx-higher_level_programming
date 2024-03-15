#!/usr/bin/python3

""" Defines a function that prints a text"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: .,? and :

    Args:
        text (str): string to be printed

    Raises:
        TypeError: text must be a string

    Examples:
        >>> text_indentation("Hello, how are you doing? do you think. you need: Time")
        Hello, how are you doing?
        do you think.
        you need:
        Time
        >>> text_indentation(3)
        Trcaeback: (most rexent call last):
            ...
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for n in range(len(text)):
        if n == 0:
            print(text[n], end='')
            continue
        if (text[n - 1] == '.' or text[n - 1] == '?' or text[n - 1] == ':' or text[n - 1] == ' ') and text[n] == ' ':
            continue
        print(text[n], end='')
        if text[n] == '.' or text[n] == '?' or text[n] == ':':
            print()
            print()
