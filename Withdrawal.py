balance = 15000
errMenu = 0

def errorMenu():
    print("What would you like to do?")
    print("1. Re-enter Withdrawal Amount")
    print("2. Check Current Balance")
    print("3. Exit")

def withdraw():
    global balance, errMenu
    WAmount = 0
    try:
        WAmount = int(input("\nEnter Withdrawal Amount: $"))
    except ValueError:
        print("Invalid Amount!\n")
        errMenu = 1
        return
    else:
        if WAmount <= 0:
            print("\nAmount must be greater than 0!")
            errMenu = 1
        elif WAmount > balance:
            print("\n!! INSUFFICIENT FUNDS !!")
            errMenu = 1
        else:
            balance = balance - WAmount
            print("\nTransaction Successful!")
    finally:
        print(f"Amount Withdrawn: ${WAmount}")
        print(f"Remaining Balance: ${balance}\n")

while True:
    if errMenu == 0:
        print("---ABC BANK ATM---")
        print("1. Withdraw Cash")
        print("2. Check Balance")
        print("3. Exit")
    else:
        errorMenu()
        errMenu = 0
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid Input!")
        continue

    if choice == 1:
        withdraw()
    elif choice == 2:
        print(f"\nCurrent Balance: ${balance}\n")
    elif choice == 3:
        print("\nExiting...")
        break
    else:
        print("Please choose the numbers 1 to 3")
