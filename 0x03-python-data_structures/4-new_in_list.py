#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return my_list[:]
    else:
        my_copied_list = my_list.copy()
        my_copied_list[idx] = element
        return my_copied_list
