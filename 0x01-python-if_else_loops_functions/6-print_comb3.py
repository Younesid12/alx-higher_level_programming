#!/usr/bin/python3
for i in range(1, 90):
    for n in range(1, i):
        if str(i).zfill(2) == ''.join(reversed(str(n).zfill(2))):
            break
    else:
        if (i != 89):
            print("{}".format(i), end=', ')
        else:
            print("{}".format(i), end= '')
