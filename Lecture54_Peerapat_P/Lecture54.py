def login():
    usernameInput = input("Enter your Username : ")
    passwordInput = input("Enter your Password : ")
    if usernameInput == "Pimpat" and passwordInput == "1234":
        showMenu()
    else:
        print("Username or Password is incorrect")
        login()

def showMenu():
    print("Done !")
    print("---- Pimpat Store ----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    MenuSelect()

def MenuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculate(int(input("Enter price : "))))
    elif userSelected == 2:
        priceCalculate()
    else:
        print("Select 1 or 2")
        MenuSelect()

    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * 7 / 100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()
