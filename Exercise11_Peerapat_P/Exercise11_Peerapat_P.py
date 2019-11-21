number = int(input("Enter a number : "))
for i in range(number):
    space = " " * (number - (i+1))
    asterisk = "*" * ((i*2)+1)
    print(space, asterisk)