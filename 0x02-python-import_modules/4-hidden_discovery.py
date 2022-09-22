#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print sorted name fom dirctory
    for name in sorted(dir(hidden_4)):
        # Print only name that do not start with __
        if name[:2] != '__':
            print("{}".format(name))
