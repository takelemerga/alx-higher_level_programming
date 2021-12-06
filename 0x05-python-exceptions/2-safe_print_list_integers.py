#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ''' handles Typeerror,ValueError and indexerror exceptions''' 
    num_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_elements += 1
        except (TypeError, ValueError, IndexError):
            continue
    print("")
    return (num_elements)
