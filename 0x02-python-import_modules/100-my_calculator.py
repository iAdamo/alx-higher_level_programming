#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    operator = "+-*/"
    flag = 0
    for each_op in operator:
        if each_op == argv[2]:
            flag = 1
    if flag == 0:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    match argv[2]:
        case "+":
            print(f"{a} {argv[2]} {b} = {add(a, b)}")
        case "-":
            print(f"{a} {argv[2]} {b} = {sub(a, b)}")
        case "*":
            print(f"{a} {argv[2]} {b} = {mul(a, b)}")
        case "/":
            print(f"{a} {argv[2]} {b} = {div(a, b)}") 
