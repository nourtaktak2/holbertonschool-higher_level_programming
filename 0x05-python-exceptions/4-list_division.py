#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    j = []
    for i in range(list_length):
        try:
            j.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            j.append(0)
            print("division by 0")
        except TypeError:
            j.append(0)
            print("wrong type")
        except IndexError:
            j.append(0)
            print("out of range")
        finally:
            pass
    return(j)
