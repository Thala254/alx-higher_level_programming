#!/usr/bin/python3
from sys import argv


def infinite_add():
    sum = 0
    for index, num in enumerate(argv):
        if index > 0:
            sum += int(num)
    print(f"{sum:d}")


if __name__ == "__main__":
    infinite_add()
