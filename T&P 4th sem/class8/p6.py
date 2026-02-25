st=input("Enter a string: ")
rst=st[::-1]
ch=input("Enter the character to find first and last occurrence: ")
first=st.find(ch)
last=rst.find(ch)
print(f"First occurrence of '{ch}' is at index {first}")
print(f"Last occurrence of '{ch}' is at index {len(st)-1-last}")