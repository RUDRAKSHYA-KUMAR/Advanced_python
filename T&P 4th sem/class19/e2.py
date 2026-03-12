class ContactBook:
    def __init__(self):
        self.contacts = {}

    # Add Contact
    def add_contact(self, name, phone):
        try:
            if not name or not phone:
                raise ValueError("Fields cannot be empty!")

            if name in self.contacts:
                raise Exception("Contact already exists!")

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number! Must be 10 digits.")

            self.contacts[name] = phone
            print("Contact added successfully!")

        except Exception as e:
            print("Error:", e)

    # Edit Contact
    def edit_contact(self, name, new_phone):
        try:
            if name not in self.contacts:
                raise Exception("Contact not found!")

            if not new_phone.isdigit() or len(new_phone) != 10:
                raise ValueError("Invalid phone number format!")

            self.contacts[name] = new_phone
            print("Contact updated successfully!")

        except Exception as e:
            print("Error:", e)

    # Search Contact
    def search_contact(self, name):
        try:
            if name not in self.contacts:
                raise Exception("Contact not found!")

            print(f"Name: {name} | Phone: {self.contacts[name]}")

        except Exception as e:
            print("Error:", e)

    # Display Contacts
    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty")
        else:
            for name, phone in self.contacts.items():
                print(name, ":", phone)


# Main Program
book = ContactBook()

while True:
    print("\n1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        book.add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to edit: ")
        phone = input("Enter new phone: ")
        book.edit_contact(name, phone)

    elif choice == "3":
        name = input("Enter name to search: ")
        book.search_contact(name)

    elif choice == "4":
        book.display_contacts()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")