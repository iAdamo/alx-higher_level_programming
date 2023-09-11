#!/usr/bin/python3
"""
1-my_list module: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/1-my_list.txt | tail -2) to test
Remove the pipeline to see full details
"""


class Mylist(list):
    """Mylist: A class that inherits from a builtin class (list)"""
    def print_sorted(self):
        """print_sorted: prints a sorted list in ascending order
        Assume all the elements of the list will be of type int
        """
        print(sorted(self))
