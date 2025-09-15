import random

# all possible characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*?"

def mainfunc():
    characters = letters + numbers + symbols
    
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("❌ Please enter a number!")
        return mainfunc()  # restart

    remove_chars = input("Enter the letters/characters you do not want to include: ")

    # remove each character individually
    for ch in remove_chars:
        characters = characters.replace(ch, "")

    if not characters:  # if user removed everything
        print("❌ No characters left to generate password!")
        return

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Your password is:", password)

    cont = input("Do you want to continue (y)? ")
    if cont.lower() == "y":
        mainfunc()
    else:
        print("Exited")

mainfunc()
