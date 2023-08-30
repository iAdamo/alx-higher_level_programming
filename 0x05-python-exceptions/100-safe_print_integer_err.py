#!/usr/bin/python3
def safe_print_integer_err(value):
    """safe_print_integer - function that print an integer

    Args:
        value: value can be any type

    Return:
        True if value has been correctly printed
        (it means the value is an integer)
        Otherwise, returns False
    """
    from sys import stderr
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as err:
        stderr.write("Exception: {}\n".format(err))
        return (False)
