print(".....Hello! welcome to the hostel NC.9......")
rn=0
while rn<6:
    name=input("Name please: ")
    per=int(input("tell me what is your entry number:"))
    if per in [1,2,3,4,5]:
        print("Congratulations! aapko milta hai apne hostel me ek room")
        rn=rn+1

    else:
        print("room is full......")
        print("VIsit again")
        break
