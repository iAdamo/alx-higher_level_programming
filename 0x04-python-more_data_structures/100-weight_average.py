#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    score, weight = (0, 0)
    for each_tuple in my_list:
        a, b = each_tuple
        score += (a * b)
        weight += b
    return (score / weight)
