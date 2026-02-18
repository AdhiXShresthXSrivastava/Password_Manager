import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password(name, password):
    with open("password.txt", "a") as f:
        f.write(f"\nThe password of {name} is {password}")
    print("The password is saved successfully.")

print("1. Generate The Password And Save\n2. Save Your Password")

try:
    option_input = int(input("Enter the option number: "))
    
    if option_input == 1:
        name_for_password = input("Enter the name for which you want to create a password: ").capitalize()
        password = generate_password()
        save_password(name_for_password, password)
        print(f"The password is {password}.")
    
    elif option_input == 2:
        name_for_password = input("Enter the name for which you want to create a password: ").capitalize()
        password_input = input(f"Enter the password for {name_for_password}: ")
        save_password(name_for_password, password_input)
    
    else:
        raise ValueError("Invalid option selected!")

except ValueError as e:
    print("Error:", e)