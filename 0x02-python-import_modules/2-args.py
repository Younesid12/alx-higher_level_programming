#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length > 1:
        print("{:d} arguemnt{:s}".format(length-1, "s:" if length > 2 else":"))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
