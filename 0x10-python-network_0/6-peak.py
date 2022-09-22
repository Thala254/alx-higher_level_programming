#!/usr/bin/python3

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return
    return search(0, len(list_of_integers) - 1, list_of_integers)

def search(l, h, int_list):
    """ quick sort algorithm """
    mid = (l + h) // 2
    if l == h:
        return int_list[l]
    if int_list[mid] < int_list[mid + 1]:
        return search(mid + 1, h, int_list)
    return search(l, mid, int_list)
