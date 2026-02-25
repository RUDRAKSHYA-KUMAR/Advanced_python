#Atm transaction system 
name=input("Enter your name: ")
password=int(input("Enter your  digit password: "))

if(name=="Rudrakshya" and password==2005):
    bal=0
    transaction1= []
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
            transaction1.append(f"Deposited: {amt}")
            print(f"Deposited {amt} successfully.")
        elif choice==2:
            amt=float(input("Enter amount to withdraw: "))
            if amt>bal:
                print("Insufficient balance.")
            else:
                bal-=amt
                transaction1.append(f"Withdrew: {amt}")
                print(f"Withdrew {amt} successfully.")
        elif choice==3:
            print(f"Current Balance: {bal}")
        elif choice==4:
            print("Transaction History:")
            for t in transaction1:
                print(t)
        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

elif(name=="Swayamjit" and password==2006):
    bal=0
    transaction2= []
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
            transaction2.append(f"Deposited: {amt}")
            print(f"Deposited {amt} successfully.")
        elif choice==2:
            amt=float(input("Enter amount to withdraw: "))
            if amt>bal:
                print("Insufficient balance.")
            else:
                bal-=amt
                transaction2.append(f"Withdrew: {amt}")
                print(f"Withdrew {amt} successfully.")
        elif choice==3:
            print(f"Current Balance: {bal}")
        elif choice==4:
            print("Transaction History:")
            for t in transaction2:
                print(t)
        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("username password mismatched. try again")


