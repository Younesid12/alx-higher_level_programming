#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if len(my_list) == 0:
        return None
    elif my_list[0] < 0:
        x = my_list[0]
    else:
        for n in my_list:
            if x < n:
                x = n
    return x
