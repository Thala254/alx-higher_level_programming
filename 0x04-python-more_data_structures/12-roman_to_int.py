#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i, ch in enumerate(roman_string):
        val = roman[ch]
        try:
            if val < roman[roman_string[i + 1]]:
                val = val * -1
        except IndexError:
            pass
        number = number + val
    return number
