username = "pimpat"
password = "1234"

keyboard = 1500
mouse = 600
monitor = 5000

print("Enter your username and password to to Enter our program")
usernameInput = input("Enter username : ")
passwordInput = input("Enter password : ")

if username == usernameInput and password == passwordInput:
    print("---Welcome to Pimpat store---")
    print("Our Products :"
          "\n 1. keyboard price : ", keyboard, "baht",
          "\n 2. mouse price : ", mouse, "baht",
          "\n 3. monitor price : ", monitor, "baht")
    selectProduct = \
        int(input("Select keyboard enter 1"
                  "\nSelect mouse enter 2"
                  "\nSelect monitor enter 3"
                  "\nEnter here : "))

    if selectProduct == 1:
        quality = int(input("Enter quality : "))
        print("keyboard price : ", keyboard, "baht", "quality : ", quality)
        print("Total : ", keyboard * quality, " baht")
    elif selectProduct == 2:
        quality = int(input("Enter quality : "))
        print("mouse price : ", mouse, "baht", "quality : ", quality)
        print("Total : ", mouse * quality, " baht")
    elif selectProduct == 3:
        quality = int(input("Enter quality : "))
        print("mouse price : ", monitor, "baht", "quality : ", quality)
        print("Total : ", monitor * quality, " baht")
    else:
        print("You must enter 1, 2, 3")

else:
    print("username or password is wrong")
