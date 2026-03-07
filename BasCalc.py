while True:
    print(f"{'Basic Calculator':-^30}")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    oper = int(input("Choice: "))
    
    if oper == 5:
        print("Bye Bye!")
        break
    num1 = int(input("1st No.: "))
    num2 = int(input("2nd No.: "))

    if oper == 1:
        print(f"Result: {num1 + num2}")
    elif oper == 2:
        print(f"Result: {num1 - num2}")
    elif oper == 3:
        print(f"Result: {num1 * num2}")
    elif oper == 4:
        if num2 == 0:
            print(f"{num1} cannot be divided by 0")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid Operator")
