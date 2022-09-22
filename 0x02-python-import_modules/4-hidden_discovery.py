#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lines = dir(hidden_4)
    for i in lines:
        if i[:2] != "__":
            print(i)
