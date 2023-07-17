#!/usr/bin/python3
def no_c(my_string):
    result = []
    for checker in my_string:
        if checker != 'c' and checker != 'C':
            result.append(checker)
        return''.join(checker)
