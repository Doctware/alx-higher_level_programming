#!/usr/bin/python3
for tens_d in range(10):
    for one_d in range(tens_d + 1, 10):
        if tens_d != one_d:
            if tens_d == 8 and one_d == 9:
                print(f"{tens_d}{one_d}")
            else:
                print(f"{tens_d}{one_d}, ", end='')
