#!/usr/bin/python3
def roman_to_int(roman_string):
    """ function that converts a Roman numeral to an integer."""
    if isinstance(roman_string, str):
        result = 0
        roman_figure = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                        'D': 500, 'M': 1000}
        roman_list = list(roman_string.upper())
        for each_str in roman_list:
            for key, value in roman_figure.items():
                if each_str == key:
                    result += value
                    break
        return (result)
