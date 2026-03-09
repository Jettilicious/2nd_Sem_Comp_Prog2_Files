while True:
    try:
        print(f"{'Basic Calculator':-^30}")
        print("1. Add")
        print("2. Sub")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print(f"{'':-^30}\n")
        oper = int(input("Choice: "))
        
        
        if oper == 5:
            print("Bye Bye!")
            break
        if oper == 1 or oper == 2 or oper == 3 or oper == 4: 
            try:
                num1 = int(input("1st No.: "))
                num2 = int(input("2nd No.: "))
            except:
                print("Invalid input/No input\n")
                continue
    
        if oper == 1:
            print(f"Result: {num1 + num2}\n")
        elif oper == 2:
            print(f"Result: {num1 - num2}\n")
        elif oper == 3:
            print(f"Result: {num1 * num2}\n")
        elif oper == 4:
            if num2 == 0:
                print(f"{num1} cannot be divided by 0\n")
            else:
                print(f"Result: {num1 / num2}\n")
        else:
            print("Invalid Operator\n")
    except:
        print("Invalid input/No input\n")
        continue
