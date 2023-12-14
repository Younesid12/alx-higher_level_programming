#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{}".format(str(n).zfill(2)))
    else:
        print("{}".format(str(n).zfill(2)), end=', ')
