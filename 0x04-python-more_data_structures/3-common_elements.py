#!/usr/bin/python3
def common_elemts(set_1, set_2):
    common_set = set(set_1) & set(set_2)
    return list(common_set)
