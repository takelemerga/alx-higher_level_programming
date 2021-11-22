#!/usr/bin/python3
def no_c(my_string):
    copy = [chr for chr in my_string if chr != 'c' and chr != 'C']
    return("".join(copy))
