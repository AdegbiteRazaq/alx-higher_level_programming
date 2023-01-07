#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    string = []
    for i in str:
        if j == n:
            j += 1
            continue
        j += 1
        string.append(i)
    return ''.join(string)
