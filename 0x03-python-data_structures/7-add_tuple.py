#!/usr/bin/python3
if __name__ != "__main__":
    exit


def add_to_tuple(_turple=()):
    if len(_turple) == 0:
        return (0, 0)
    if len(_turple) < 2:
        for each_item in _turple:
            if each_item <= 0 or each_item >= 0:
                (a, b) = each_item, 0
            return (a, b)
    if len(_turple) == 2:
        return (_turple)
    if len(_turple) > 2:
        return (_turple[0], _turple[1])


def add_tuple(tuple_a=(), tuple_b=()):
    """ function that adds 2 tuples

        Args:
        tuple_a: first tuple
        tuple_b: second tuple

        Return:
        a tuple with 2 integers
    """
    a, b = add_to_tuple(tuple_a)
    c, d = add_to_tuple(tuple_b)

    (e, f) = a + c, b + d
    return (e, f)
