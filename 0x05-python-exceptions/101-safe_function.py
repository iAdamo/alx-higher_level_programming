#!/usr/bin/python3
def safe_function(fct, *args):
    """safe_function - function that execute a function safely

    Args:
        fct: will always be a pointer to a function
        *args: a tuple of positional arguments

    Return:
        result of the function
    """
    from sys import stderr
    try:
        return (fct(*args))
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
