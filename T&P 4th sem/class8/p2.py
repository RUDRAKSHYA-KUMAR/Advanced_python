upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
countUpper=0
countLower=0
st=input("Enter a string: ")
for char in st:
    if char in upper:
        countUpper+=1
    elif char in lower:
        countLower+=1

print("Number of uppercase characters:", countUpper)
print("Number of lowercase characters:", countLower)