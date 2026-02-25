sent=input("Enter a sentence: ")
words=sent.split(" ")
var1=set()
for word in words:
    if word not in var1:
        var1.add(word)

    else:
        continue
print("Unique words in the sentence are:", var1)
