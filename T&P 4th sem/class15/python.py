"""aaj ka kaam- 
online shoping cart
product catelog
shoping cart add, remove
checkin, checkout
discount """

list_of_prod = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Smartphone", "price": 50000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1500},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Monitor", "price": 12000},
    {"id": 7, "name": "Printer", "price": 7000},
    {"id": 8, "name": "Webcam", "price": 3000},
    {"id": 9, "name": "Speakers", "price": 4000},
    {"id": 10, "name": "External Hard Drive", "price": 6000}
]

print("Welcome to amazlipcart online store!")
print("We have these following products available:")
cart=[]
for pro in list_of_prod:#showing products
    print("ID:", pro["id"], ", Name:", pro["name"], ", Price: Rs.", pro["price"])
while True:#inserting products to cart
    x=input("\nEnter product ID to add to your cart. Type 'done' when finished: ")
    while x.lower() != 'done':
        if x in [ str(prod["id"]) for prod in list_of_prod]:
            cart.append(int(x))
            print("Product ID", x, "added to your cart.")
            break     
        else:
            print("Invalid product ID. Please try again.")
            break
    
    if x.lower() == 'done':
        print("Thank you for shopping with us!")
        break
#showing whatever is in cart
print("You have these items in your cart:")
for item in cart:
    for prod in list_of_prod:
        if prod["id"] == item:
            print("ID:", prod["id"], ", Name:", prod["name"], ", Price: Rs.", prod["price"])
            break
#asking for removal of product from cart
rem=input("\nEnter product ID you want to remove from the cart or type none for no removal: ")
if rem.lower() != 'none':
    if int(rem) in cart:
        cart.remove(int(rem))
        print("Product ID", rem, "removed from your cart.")
    else:
        print("Product ID not found in your cart.")
sum=0 #calculating total amount
for item in cart:
    for prod in list_of_prod:
        if prod["id"] == item:
            
            sum+=prod["price"]
            break
print("\nYour total amount is: Rs.", sum)
#asking for discount coupon
dis=int(input("ENter how much discount coupon you have in percentage: "))
print("\nYour total amount will be: ",sum*(1-dis/100))#showing the net ammount

print("\nThank you for shopping with amazlipcart online store!")
