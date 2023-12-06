#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list[:]
    for item in range(len(my_new_list)):
        if my_new_list[item] == search:
            my_new_list[item] = replace
    return my_new_list
