#!/usr/bin/python3
def roman_to_int(roman_string):
    """ function that converts a Roman numeral to an integer."""
    if isinstance(roman_string, str):
        num = []
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
        roman_list = list(roman_string.upper())
        for figure in roman_list:
            for key, value in roman_dict.items():
                if figure == key:
                    num.append(value)
        for i in range(len(num)):
            if i == 0:
                result = num[i]
            elif num[i] > num[i - 1]:
                result = num[i] - result
            else:
                if i == (len(num) - 2) and (num[i + 1] > num[i]):
                    result += (num[i + 1] - num[i])
                    return (result)
                result += num[i]
        return (result)
