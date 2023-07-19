#!/usr/bin/python3
def weight_average(my_list=[]):
    tweight = 0
    tscore = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        tweight = tweight + weight
        tscore += scpre * weight
    return tscore / tweight
