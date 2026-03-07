users = []

while True:
    print("---User Menu---")
    print("1. Show")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete user")
    print("5. Exit")
    choice = int(input("Choice: "))
    
    if choice == 1:
        if len(users) == 0:
            print("No users found!")
        else:
            print(users)
    elif choice == 2:
        add = input("Add new user: ")
        users.append(add)
        print(users)
    elif choice == 3:
        update = input("What user do you want to update?: ")
        if update in users:
            index = users.index(update)
            newUser = input("Enter new user: ")
            users[index] = newUser
            print(users)
    elif choice == 4:
        delete = input("What user to delete?: ")
        if delete in users:
            users.remove(delete)
            print(users)
    elif choice == 5:
        print("Bye Bye...")
        break
    else:
        print("That's not in the choices")