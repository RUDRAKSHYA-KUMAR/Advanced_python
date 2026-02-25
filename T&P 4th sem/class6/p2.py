#transaction wala sawal
bal=0
transaction= []
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        amt=float(input("Enter amount to deposit: "))
        bal+=amt
        transaction.append(f"Deposited: {amt}")
        print(f"Deposited {amt} successfully.")
    elif choice==2:
        amt=float(input("Enter amount to withdraw: "))
        if amt>bal:
            print("Insufficient balance.")
        else:
            bal-=amt
            transaction.append(f"Withdrew: {amt}")
            print(f"Withdrew {amt} successfully.")
    elif choice==3:
        print(f"Current Balance: {bal}")
    elif choice==4:
        print("Transaction History:")
        for t in transaction:
            print(t)
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


        #HW- isme password wala feature add karna hai