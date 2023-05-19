#!/usr/bin/python3

def weight_average(my_list=[]):

    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg_weight = 0
    score = 0
    for tup in my_list:
        avg_weight += (tup[0] * tup[1])
        score += tup[1]
    return (avg_weight / score)
