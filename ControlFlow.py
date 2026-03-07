for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or j == 0:
            print("* ", end='')
        else:
            print("  ", end='')
    print("* ")
print("\n\n\n")

k = 10

for i in range(11):
    for j in range(k) :
        print("* ", end='')
    k -= 1
    print("* ")
