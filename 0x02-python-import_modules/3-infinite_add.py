#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argc = len(args) - 1
    total = 0
    if argc == 0:
        print(total)
    else:
        for i in range(0, argc):
            total = total + int(args[i + 1])
        print(total)
