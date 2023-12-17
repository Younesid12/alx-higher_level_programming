#!/usr/bin/python3
for i in range(1, 90):
    for n in range(1, i+1):
        if str(i).zfill(2) == ''.join(reversed(str(n).zfill(2))):
            break
    else:
        if (i != 89):
            print("{}".format(str(i).zfill(2)), end=', ')
        else:
            print("{}".format(str(i).zfill(2)))
