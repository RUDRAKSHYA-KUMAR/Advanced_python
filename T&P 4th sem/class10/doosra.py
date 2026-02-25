var1=set()
var2=set()
n=int(input("Enter how many students you want to enter:"))
for i in range(n):
  name=input("Enter the name of the student:")
  if name in var1:
      print("Name already exists, shifting to var2")
      var2.add(name)
  else:
      print(name, "Entry allowed")
      var1.add(name)

print("Students in set original: ",var1)
print("Students in set duplicate: ",var2)