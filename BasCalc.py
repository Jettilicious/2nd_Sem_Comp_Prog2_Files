while True:
    num1 = 0
    num2 = 0
    oper = ''
    total = 0
    print(f"{'Basic Calculator':-^30}")
    print("1. Continue")
    print("2. Exit")
    choice = int(input("Choice: "))

    if choice == 2:
        print("Bye Bye!")
        break

    num1 = int(input("1st No.: "))
    oper = input("Operator(+,-,*,/): ")
    num2 = int(input("2nd No.: "))

    if oper == '+':
        total = num1 + num2
        print(f"Result: {total}")
    elif oper == '-':
        total = num1 - num2
        print(f"Result: {total}")
    elif oper == '*':
        total = num1 * num2
        print(f"Result: {total}")
    elif oper == '/':
        if num2 == 0:
            print(f"{num1} cannot be divided by 0")
        else:
            total = num1 / num2
            print(f"Result: {total}")
    else:
        print("Invalid Operator")