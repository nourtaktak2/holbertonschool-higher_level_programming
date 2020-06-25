#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        j = a / b
        return(a / b)
    except ZeroDivisionError:
        j = None
        return(None)
    finally:
        print("Inside resul: {}".format(j))
        
