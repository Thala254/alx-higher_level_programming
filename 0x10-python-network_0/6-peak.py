#!/usr/bin/python3
""" modue containing peak function """

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return
    return search(0, len(list_of_integers) - 1, list_of_integers)


def search(first, last, int_list):
    """ quick sort algorithm """
    mid = (first + last) // 2
    if first == last:
        return int_list[last]
    if int_list[mid] < int_list[mid + 1]:
        return search(mid + 1, last, int_list)
    return search(first, mid, int_list)
