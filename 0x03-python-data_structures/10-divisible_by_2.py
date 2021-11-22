#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = []
    i = 0
    while (i < len(my_list)):
        if my_list[i] % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return (even)


ls = [2, 4, 7, 22, 90, 75]
divisible_by_2(ls)
