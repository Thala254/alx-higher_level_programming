#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiple = {}
    if a_dictionary:
        for k, v in a_dictionary.items():
            multiple.update({k: v * 2})
        return multiple
