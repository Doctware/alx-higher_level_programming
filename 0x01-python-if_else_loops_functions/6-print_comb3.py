#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if i == j:
            continue
        if i == 8 and j == 9:
            print("{}".format(str(i) + str(j)))
        elif int(str(i) + str(j)) < int(str(j) + str(i)):
            print("{}, ".format(str(i) + str(j)), end="")
        else:
            print("{}, ".format(str(j) + str(i)), end="")
