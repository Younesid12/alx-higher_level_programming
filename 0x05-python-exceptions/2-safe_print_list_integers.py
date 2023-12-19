#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_result = 0
    i = 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_result += 1
        except IndexError:
            break
        i += 1
        print()
        return printed_result
