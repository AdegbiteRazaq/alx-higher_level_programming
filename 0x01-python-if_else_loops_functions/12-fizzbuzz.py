#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            i = 'fizzbuzz'
        elif i % 5 == 0:
            i = 'buzz'
        elif i % 3 == 0:
            i = 'fizz'
        print('{}'.format(i), end=' ')
