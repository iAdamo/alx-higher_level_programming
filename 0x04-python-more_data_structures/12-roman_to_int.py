#!/usr/bin/python3
def roman_to_int(roman_string):
    """ function that converts a Roman numeral to an integer

        Args:
        roman_string: a string of roman figures

        Return:
        Integer
    """
    # check if roman_string is of type str else return 0
    if type(roman_string) is not str:
        return (0)
    num = []
    # Create a dictionary of all roman figures
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    # make a list of all inputs either lower or uppercase useful
    roman_list = list(roman_string.upper())
    # loop through each roman_list and make a list of thier integer
    # representations
    for figure in roman_list:
        for key, value in roman_dict.items():
            if figure == key:
                num.append(value)
    # compare each roman integer
    for i in range(len(num)):
        # if one input or the first one should always be positive
        if i == 0:
            result = num[i]
        # else if the current index is > the previous one, do subtraction
        elif num[i] > num[i - 1]:
            result = num[i] - result
        # else, if equals to each other or the current index is lower
        # than the prev one
        else:
            # case for the last two index, if the last index is > the prev one
            # always substract them and return as it's the end of the loop
            if i == (len(num) - 2) and (num[i + 1] > num[i]):
                result += (num[i + 1] - num[i])
                return (result)
            # same as line 37 comment
            result += num[i]
    # return result
    return (result)
