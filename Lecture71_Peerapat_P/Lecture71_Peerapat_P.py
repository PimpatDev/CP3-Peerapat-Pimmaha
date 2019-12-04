menuList = []
priceList = []
total = 0
def showBill():
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print("Total : ", sum(priceList))

while True:
    menuName = input("Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Enter Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()


