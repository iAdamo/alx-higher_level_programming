#!/usr/bin/python3
if __name__ != "__main__":
    exit


def only_diff_elements(set_1, set_2):
    if len(set_1) == 0 and len(set_2) == 0:
        return {}
    c_set = set()
    for each_item in set_1:
        if each_item in set_2:
            c_set.add(each_item)
    for each_item in set_1:
        set_2.add(each_item)
    for each_item in c_set:
        if each_item in set_2:
            set_2.discard(each_item)
    return set_2
