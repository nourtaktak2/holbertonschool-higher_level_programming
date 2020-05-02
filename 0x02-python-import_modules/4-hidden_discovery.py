#!usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    x = "__"
    for i in (dir(hidden_4)):
        if x not in i:
            print(i)
