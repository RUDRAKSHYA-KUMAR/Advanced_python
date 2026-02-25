st1=input("Enter first string: ")
st2=input("Enter second string: ")
if len(st1)==len(st2):
    for i in st1:
        if i not in st2:
            print("Strings are not anagrams.")
            break
    else:
        print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")