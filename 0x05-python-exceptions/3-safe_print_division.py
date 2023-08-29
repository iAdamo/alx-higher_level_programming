#!/usr/bin/python3
def safe_print_division(a, b):
    """safe_print_division - divides 2 integers and prints the result

    Args:
        a: integer one
        b: integer two

    Return:
        the value of the division, otherwise: None
    """
    try:
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result: {}".format(a))
        return (a)
