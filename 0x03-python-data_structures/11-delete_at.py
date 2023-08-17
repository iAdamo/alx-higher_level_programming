#!/usr/bin/python3
if __name__ != "__main__":
    exit


def delete_at(my_list=[], idx=0):
    if len(mylist) == 0:
        return None
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    for i in range(len(my_list)):
        if i == idx:
            continue
        new_list.append(my_list[i])
    return (new_list)
