#password strength checker

password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short. It should be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password should contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password should contain at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password should contain at least one digit.")
else:
    print("Password is strong.")