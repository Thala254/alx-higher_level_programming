#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            delete_keys.append(k)
    for i in delete_keys:
        del a_dictionary[i]
    return a_dictionary
