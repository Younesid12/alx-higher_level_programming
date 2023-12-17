#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            string = string + chr(ord(char) - 32)
        else:
            string = string + char
    print("{}".format(string))
