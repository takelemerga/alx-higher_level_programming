#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ''' handles Typeerror,ValueError and indexerror exceptions'''

    num_elements = 0
    for ele in range(0, x):
        try:
            print("{:d}".format(my_list[ele]), end="")
            num_elements += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print("")
    return (num_elements)
