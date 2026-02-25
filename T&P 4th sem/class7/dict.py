rudra= {
    "name" : "Rudrakshya",
    "age" : 21,
    "city" : "Bangalore",
    "hobbies" : ["coding", "gaming", "traveling"],
}

for key, values in rudra.items():
    print(key, ":", values)
    if key == "hobbies":
        for hobby in values:
            print(hobby.capitalize())