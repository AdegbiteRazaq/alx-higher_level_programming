#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if(i < j and i != 8):
            print('{0}{1}'.format(i, j), end=', ')
        elif (i < j):
            print('{0}{1}'.format(i, j))
