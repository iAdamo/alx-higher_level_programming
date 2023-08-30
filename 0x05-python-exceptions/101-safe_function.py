#!/usr/bin/python3
def safe_function(fct, *args):
    """safe_function - function that execute a function safely

    Args:
        fct: will always be a pointer to a function
        *args: a tuple of positional arguments

    Return:
        result of the function
    """
    try:
        from sys import stderr
        try:
            return (fct(args[0], args[1]))
        except ZeroDivisionError as zerr:
            stderr.write("Exception: {}\n".format(zerr))
            return (None)
        except TypeError as terr:
            stderr.write("Exception: {}\n".format(terr))
            return (None)
        except IndexError as ierr:
            stderr.write("Exception: {}\n".format(ierr))
            return (None)
    except ImportError as imerr:
        stderr.write("Exception: {}\n".format(imerr))
        return (None)
