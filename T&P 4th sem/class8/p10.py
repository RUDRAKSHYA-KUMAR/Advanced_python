st = input("Enter a string: ")

n = len(st)
pal = True

for i in range(n // 2):
    if st[i] != st[n - 1 - i]:
        pal = False
        break

if pal:
    print("Palindrome hai")
else:
    print("Palindrome nahi hai")
