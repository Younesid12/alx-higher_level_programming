#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for char in sorted(a_dictionary):
        print("{}: {}".format(char, a_dictionary[char]))
