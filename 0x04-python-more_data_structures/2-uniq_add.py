#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    j = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            j += i
    return j
