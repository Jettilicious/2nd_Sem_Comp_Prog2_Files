class Cart:
    def __init__(self):
        self.item = {}

    def addItem(self, name, price, quantity):
        if name in self.item:
            self.item[name]["quantity"] += quantity
            print(f"Quantity of {name} increased to {self.item[name]['quantity']}\n")
        else:
            self.item[name] = {"price": price, "quantity": quantity}
            print(f"Added {name} | Price: {price} each | Quantity: {self.item[name]['quantity']}\n")
    def deleteItem(self, name):
        if name in self.item:
            price = self.item[name]['price']
            quantity = self.item[name]['quantity']
            self.item.pop(name)
            print(f"\nRemoved {name} | Price: ${price:.2f} | Quantity: {quantity}\n")
        else:
            print("Item not found\n")
    def viewCart(self):
        if len(self.item) == 0:
            print("Empty Cart\n")
        else:
            total = 0
            for name, data in self.item.items():
                qtotal = float(data['price'] * data['quantity'])
                total += qtotal
                print(f"-{name} | ${data['price']:.2f} x{data['quantity']} = ${qtotal:.2f}")
            print(f"Current Total: ${total}\n")
    def checkOut(self):
        if len(self.item) == 0:
            print("No items for Checkout\n")
        else:
            total = 0
            for name, data in self.item.items():
                print(f"{name}: ${data['price']:.2f} x{data['quantity']}")
                fprice = data['price'] * data['quantity']
                total += fprice
            print(f"Total Amount: ${total:.2f}\n")
cart = Cart()

while True:
    try:
        print(f"{'Shoping Cart':=^40}")
        print("1. View Cart")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Checkout/Exit\n")
        choice = int(input("Choice: "))

        #VIEW
        if choice == 1:
            cart.viewCart()
        #ADD
        elif choice == 2:
            try:
                max = int(input("How many items to add to cart: "))
                i = 0
                if max == 0:
                    print("Cannot add no items\n")
                    continue
            except ValueError:
                print("Invalid Input\n")
                continue
            while max > i:
                try:
                    name = input(f"Add Item No.{i+1}: ")
                    if not name:
                        raise ValueError
                    elif name in cart.item:
                        quantity = int(input(f"How many?: "))
                        cart.addItem(name, cart.item[name]['price'], quantity)
                    else:
                        price = float(input("Add Price: "))
                        quantity = int(input(f"How many?: "))
                        cart.addItem(name, price, quantity)
                    i += 1
                except ValueError:
                    print("Invalid Input\n")
                    continue
        #REMOVE
        elif choice == 3:
            cart.viewCart()
            if len(cart.item) != 0: 
                delete = input("Which Item to delete?: ")
                cart.deleteItem(delete)
        #CHECKOUT
        elif choice == 4:
            cart.checkOut()
            break
        #CHOICEVALIDITY
        else:
            print("Invalid Choice")
            print(" ")
    except ValueError:
        print("Invalid Input\n")

        continue

