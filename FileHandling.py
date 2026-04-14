import os

def append(message, conversation):
    with open(conversation + ".txt", "a") as f:
        f.write("\n" + message)
    f.close()

while True:
    conversation = ""
    try:
        print("\n---Messaging App---")
        print("1. Send Message")
        print("2. View Message")
        print("3. Exit")

        choice = int(input("Choose: "))
    except ValueError:
        print("\nInvalid Input!")
        continue

    if choice == 1:
        try:
            conversation = str(input("Enter a Conversation: "))
        except ValueError:
            print("\nInvalid Input")
        else:
            if os.path.exists(conversation + ".txt"):
                try:
                    print("\nConversation Found!")
                    message = str(input("Message: "))
                except ValueError:
                    print("Bruh")
                else:
                    if not message.strip():
                        print("\nInvalid Input")
                    else:
                        append(message, conversation)
            elif not conversation.strip():
                print("\nInvalid Input")
            else:
                print("\nNo Loaded Conversations Found!")
                print("Creating New Conversation...")
                f = open(conversation + ".txt", "w")
                f.write("Welcome to ABC Messaging APP")
                print("File Created Succesfully")
                f.close()
    elif choice == 2:
        try:
            conversation = str(input("Enter a Conversation: "))
        except ValueError:
            print("\nInvalid Input")
        else:
            if os.path.exists(conversation + ".txt"):
                with open(conversation + ".txt", "r") as f:
                    read = f.read()
                    print("\n")
                    print(read)
                f.close()
            elif not conversation.strip():
                print("\nInvalid Input")
            else:
                print("\nFile Not Found!")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Nuh-uh")