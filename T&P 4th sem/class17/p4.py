books={
    101:{"name":"Python for Beginners","author":"John Doe","availability":True},
    102:{"name":"Data Science with Python","author":"Jane Smith","availability":False},
    103:{"name":"Machine Learning Basics","author":"Alice Johnson","availability":True},
    104:{"name":"Deep Learning with Python","author":"Bob Brown","availability":False},
    105:{"name":"Python for Data Analysis","author":"Charlie Davis","availability":True},
    106:{"name":"Python Cookbook","author":"David Wilson","availability":False},
    107:{"name":"Fluent Python","author":"Emily Clark","availability":True},
    108:{"name":"Automate the Boring Stuff with Python","author":"Frank Miller","availability":False},
    109:{"name":"Python Crash Course","author":"Grace Lee","availability":True},
    110:{"name":"Effective Python","author":"Henry Taylor","availability":False}
    }

print("Welcome to the Python Book Library!")
members=["Harish","Rudra","Sashi","Suresh","Ramesh","Mahesh","Naresh"]

m=input("Enter your name: ")
if m in members:
    print("Welcome",m,"! Here is the listed books in the library.")
    for key,value in books.items():
        print("ID:", key, ", Name:", value["name"])
    id=int(input("\nEnter the ID of the book you want to borrow: "))
    if id in books:
        if books[id]["availability"]==True:
            print("You have successfully borrowed", books[id]["name"])
            books[id]["availability"]=False
            print("The book is now marked as unavailable, you can keep this book for 15 days.")
        else:
            print("Sorry, the book is currently unavailable.")

else:
    print("Sorry you are not a member od the library. You have to register first to borrow books")
    c=input("Do you want to register? (y/n): ")
    if c in "yY":
        name=input("Enter your name: ")
        members.append(name)
        print("Congratulations! You are now a member of the library. You can borrow books now.")
        print("Welcome",m,"! Here is the listed books in the library.")
        for key,value in books.items():
            print("ID:", key, ", Name:", value["name"])
        id=int(input("\nEnter the ID of the book you want to borrow: "))
        if id in books:
            if books[id]["availability"]==True:
                print("You have successfully borrowed", books[id]["name"])
                books[id]["availability"]=False
                print("The book is now marked as unavailable, you can keep this book for 15 days.")
            else:
                print("Sorry, the book is currently unavailable.")
    elif c in "nN":
        print("Alright then, visit again when you want to register.")

    
