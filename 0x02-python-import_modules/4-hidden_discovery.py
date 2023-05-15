#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # To prints all the names defined by the compiled module hidden_4.pyc

    for name in dir(hidden_4):
        if name[0] != '-' and name[1] != '-':
            print(name)
