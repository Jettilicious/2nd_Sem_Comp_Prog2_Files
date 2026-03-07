def checking(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        print(f"{num1}, {num2}, and {num3} are all equal")
    elif num1 > num2 and num1 > num3:
        print(f"Random Number 1: {num1} is the largest number")
    elif num2 > num1 and num2 > num3:
        print(f"Random Number 2: {num2} is the largest number")
    else:
        print(f"Random Number 3: {num3} is the largest number")

num1 = int(input('Enter a random number 1: '))
num2 = int(input('Enter a random number 2: '))
num3 = int(input('Enter a random number 3: '))

checking(num1, num2, num3)