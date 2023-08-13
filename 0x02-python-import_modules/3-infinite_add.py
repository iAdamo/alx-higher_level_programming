#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print(f"0")
    elif len(argv) > 1:
        total = 0
        for each_int in argv:
            if each_int == argv[0]:
                continue
            else:
                num = int(each_int)
                total += num
        print(total)
