import time

class Bank:
    def __init__(self):
        self.accounts = {
            1001: 5000,
            1002: 8000,
            1003: 12000
        }

    # Display Accounts
    def show_accounts(self):
        print("\nAccount Details:")
        for acc, bal in self.accounts.items():
            print(f"Account {acc} : Balance = {bal}")

    # Transfer Money
    def transfer(self, sender, receiver, amount):
        try:
            start = time.time()

            # Check account numbers
            if sender not in self.accounts or receiver not in self.accounts:
                raise Exception("Incorrect account number!")

            # Simulate processing delay
            time.sleep(2)

            # Transaction timeout check
            if time.time() - start > 5:
                raise TimeoutError("Transaction timed out!")

            # Overdraft check
            if self.accounts[sender] < amount:
                raise Exception("Overdraft error! Insufficient balance.")

            # Perform transaction
            self.accounts[sender] -= amount
            self.accounts[receiver] += amount

            print("Transaction successful!")

        except TimeoutError as t:
            print("Error:", t)

        except Exception as e:
            print("Error:", e)


# Main Program
bank = Bank()

while True:
    print("\n1. Show Accounts")
    print("2. Transfer Money")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.show_accounts()

    elif choice == "2":
        try:
            sender = int(input("Sender Account: "))
            receiver = int(input("Receiver Account: "))
            amount = int(input("Amount: "))

            bank.transfer(sender, receiver, amount)

        except ValueError:
            print("Invalid input! Please enter numbers.")

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")