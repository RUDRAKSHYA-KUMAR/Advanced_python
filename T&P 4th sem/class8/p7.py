st = input("Enter a string: ")

vowels = "aeiouAEIOU"

for v in vowels:
    st = st.replace(v, "")

print("String after removing vowels:", st)

