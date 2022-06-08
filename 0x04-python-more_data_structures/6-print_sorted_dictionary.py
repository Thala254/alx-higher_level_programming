#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    if a_dictionary:
        for k, v in a_dictionary.items():
            keys.append(k)

        keys.sort()
        for i in keys:
            print(f"{i}: {a_dictionary[i]}")
