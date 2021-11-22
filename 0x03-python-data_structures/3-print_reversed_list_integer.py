#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list = my_list[::-1]
    for i in range(len(list)):
        print(list[i])


list = [1, 2, 3, 4, 5]
print_reversed_list_integer(list)
