rooms={
    101 : None,
    102 : None,
    103 : None,
    104 : None,
    105 : None
}

inRoom = set()
emptied = set()
while True:
    name = input("Enter your name: ")
    for i in rooms:
        if rooms[i] is None:
            rooms[i] = name
            inRoom.add(name)
            print("Room allocated to", name, "jao aish karo")
            break  
    else:
        print("Room full tata bye bye")
        break

print("The people present in room: ",inRoom)
print("\n")
for person in rooms:
    print("The room",person," is occupied by", rooms[person])

n=int(input("Enter the room number you want to vacate: "))
if rooms[n] !=None:
    rooms[n]=None
    x=input("Room emptied successfully. tell me if you want to book that room(y/n): ")
    if x in "yY":
        naam=input("Enter your name: ")
        rooms[n] = naam
        print("Room allocated to ", naam)
    elif x in "nN":
        print("alright then room emptied without alloting to someone")
        print("The removed people are: ",emptied)
    else:
        print("The room is already empty: ")

