
class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

class DuplicateProductError(Exception):
    pass


class Inventory:
    def __init__(self):
        self.products = {}

    
    def add_product(self, pid, name, quantity):
        try:
            if pid in self.products:
                raise DuplicateProductError("Product ID already exists!")

            self.products[pid] = {"name": name, "quantity": quantity}
            print("Product added successfully!")

        except DuplicateProductError as e:
            print("Error:", e)


    def sell_product(self, pid, qty):
        try:
            if pid not in self.products:
                raise InvalidProductIDError("Invalid Product ID!")

            if self.products[pid]["quantity"] < qty:
                raise OutOfStockError("Not enough stock available!")

            self.products[pid]["quantity"] -= qty
            print("Product sold successfully!")

        except (InvalidProductIDError, OutOfStockError) as e:
            print("Error:", e)

    
    def display(self):
        print("\nInventory List:")
        for pid, data in self.products.items():
            print(pid, "-", data["name"], "- Stock:", data["quantity"])



inv = Inventory()

while True:
    print("\n1. Add Product")
    print("2. Sell Product")
    print("3. Show Inventory")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        qty = int(input("Enter Quantity: "))
        inv.add_product(pid, name, qty)

    elif choice == "2":
        pid = input("Enter Product ID: ")
        qty = int(input("Enter Quantity to sell: "))
        inv.sell_product(pid, qty)

    elif choice == "3":
        inv.display()

    elif choice == "4":
        print("Exiting...")
        break

    else:

        print("Invalid choice!")
