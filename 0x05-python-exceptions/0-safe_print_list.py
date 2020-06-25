#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in my_list:
            if j <= x - 1:
                print("{}".format(i), end="")
                j += 1
        print()
        return(j)
    except:
        j = 0
        for i in my_list:
            print("{}".format(i), end="")
            j += 1
        print()
        return(j)
