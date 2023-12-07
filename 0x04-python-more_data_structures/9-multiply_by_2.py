#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    keys = list(dic.keys())

    for i in keys:
        dic[i] *= 2
    return (dic)
