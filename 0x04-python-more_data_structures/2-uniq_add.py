#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    if my_list:
        for i in my_list:
            uniq.add(i)
    return sum(uniq)
