def vatCaculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print("Total price : ", vatCaculate(float(input("Enter price : "))))