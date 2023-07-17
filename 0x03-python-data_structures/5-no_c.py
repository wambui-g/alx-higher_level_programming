#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for checker in my_string:
        if checker != 'c' and checker != 'C':
            result += checker
        return result
