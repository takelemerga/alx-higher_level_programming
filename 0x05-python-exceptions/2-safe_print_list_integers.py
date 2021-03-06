#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num_elements = 0
    for ele in range(0, x):
        try:
            print("{:d}".format(my_list[ele]), end="")
            num_elements += 1
        except (TypeError, ValueError):
            continue
    print("")
    return num_elements
