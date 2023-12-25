#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if my_list[0] < 0 and len(my_list) != 0:
        x = my_list[0]
    elif len(my_list) == 0:
        return None
    else:
        for n in my_list:
            if x < n:
                x = n
    return x
