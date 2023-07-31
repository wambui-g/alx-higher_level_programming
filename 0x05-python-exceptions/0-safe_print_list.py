#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    num_elements_printed = 0;
    try:
        for element in my_list:
            if num_elements_printed < x:
                print(element, end=' ')
                num_elements_printed += 1
    except:
        pass

    print()
    return num_elements_printed
