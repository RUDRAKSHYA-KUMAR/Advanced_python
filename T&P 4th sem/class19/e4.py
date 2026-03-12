class Ecommerce:
    def __init__(self):
        self.products = {
            "Laptop": {"price": 60000, "stock": 5},
            "Phone": {"price": 20000, "stock": 10},
            "Headphones": {"price": 2000, "stock": 15}
        }
        self.orders = []

    # Place Order
    def place_order(self, product, payment, coupon=None):
        try:
            if product not in self.products:
                raise Exception("Product not found!")

            if self.products[product]["stock"] == 0:
                raise Exception("Out of stock!")

            valid_payments = ["UPI", "Card", "Cash"]
            if payment not in valid_payments:
                raise Exception("Invalid payment method!")

            price = self.products[product]["price"]

            # Coupon handling
            if coupon:
                if coupon != "SAVE10":
                    raise Exception("Invalid coupon code!")
                price *= 0.9

            self.products[product]["stock"] -= 1
            self.orders.append(product)

            print(f"Order placed successfully! Amount paid: {price}")

        except Exception as e:
            print("Error:", e)

    # Return Order
    def return_order(self, product):
        try:
            if product not in self.orders:
                raise Exception("Order not found!")

            self.orders.remove(product)
            self.products[product]["stock"] += 1

            print("Product returned successfully!")

        except Exception as e:
            print("Error:", e)

    # Refund
    def refund(self, product):
        try:
            if product not in self.products:
                raise Exception("Invalid product for refund!")

            price = self.products[product]["price"]
            print(f"Refund processed: {price}")

        except Exception as e:
            print("Error:", e)


# Main Program
shop = Ecommerce()

while True:
    print("\n1. Place Order")
    print("2. Return Order")
    print("3. Refund")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        payment = input("Payment method (UPI/Card/Cash): ")
        coupon = input("Enter coupon (or press enter): ")

        shop.place_order(product, payment, coupon)

    elif choice == "2":
        product = input("Enter product to return: ")
        shop.return_order(product)

    elif choice == "3":
        product = input("Enter product for refund: ")
        shop.refund(product)

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")