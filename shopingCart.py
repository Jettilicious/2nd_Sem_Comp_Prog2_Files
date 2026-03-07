class Cart:
    def __init__(self):
        self.item = {}

    def addItem(self, name, price):
        self.item[name] = price
    
    def deleteItem(self, name):
        if name in self.item:
            self.item.pop(name)
            print(f"Removed {name}, Priced: ${price:.2f}")
        else:
            print("Item not found")
    def viewCart(self):
        if len(self.item) == 0:
            print("Empty Cart")
        else:
            for name, price in self.item.items():
                print(f"{name}: ${price:.2f}")
    def checkOut(self):
        if len(self.item) == 0:
            print("No items for Checkout")
        else:
            for name, price in self.item.items():
                print(f"{name}: ${price:.2f}")
            total = 0
            for name, price in self.item.items():
                total += price
            print(f"Total Amount: ${total:.2f}")
cart = Cart()

while True:
    print(f"{'Shoping Cart':=^40}")
    print("1. View Cart")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. Checkout/Exit")
    choice = int(input("Choice: "))
    print(" ")

    #VIEW
    if choice == 1:
        cart.viewCart()
        print(" ")
    #ADD
    elif choice == 2:
        max = int(input("How many items to add to cart: "))
        for i in range(max):
            name = input(f"Add Item No.{i+1}: ")
            price = float(input("Add Price: "))
            cart.addItem(name, price)
        print(" ")
    #REMOVE
    elif choice == 3:
        delete = input("Which Item to delete?: ")
        cart.deleteItem(delete)
        print(" ")
    #CHECKOUT
    elif choice == 4:
        cart.checkOut()
        break
    #CHOICEVALIDITY
    else:
        print("Invalid Choice")
        print(" ")