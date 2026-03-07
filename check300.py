check = 300

def checking(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        print(f"{numOne}, {numTwo}, and {numThree} are all equal")
    elif num1 <= num2 and num1 <= num3:
        print(f"Random Number 1: {numOne} is closer to 300")
    elif num2 <= num1 and num2 <= num3:
        print(f"Random Number 2: {numTwo} is closer to 300")
    else:
        print(f"Random Number 3: {numThree} is closer to 300")
    

print(f"Find The Closest Number to {check}")
numOne = int(input('Enter a random number 1: '))
numTwo = int(input('Enter a random number 2: '))
numThree = int(input('Enter a random number 3: '))

num1 = abs(check - numOne)
num2 = abs(check - numTwo)
num3 = abs(check - numThree)

checking(num1, num2, num3)