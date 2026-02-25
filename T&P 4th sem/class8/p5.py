st=input("Enter a string: ")
for ch in st:
    count=0
    for ch2 in st:
        if ch == ch2:
            count += 1
    print(f"Character '{ch}' occurs {count} times in the string.")