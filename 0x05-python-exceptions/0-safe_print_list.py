#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_number = 0
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            real_number += 1
        except IndexError:
            break
        i += 1
    print()
    return real_number
