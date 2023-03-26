'''Login&Menu'''
UserName = input("Username")
PassWord = input("Password")
Order1 = int(50)
Order2 = int(50)
Order3 = int(80)
Order4 = int(80)

'''Menu'''
if UserName == "admin" and PassWord == "1":
    print("Welcome to Restaurant")
    print("---Menu---")
    print("1. Papaya Salad: 50 THB")
    print("2. Papaya salad w/ dried salted prawns: 50THB" )
    print("3. Grilled pork  blade shoulder: 80THB")
    print("4. Grilled beef: 80THB")
    Order = int(input("Order"))
    if Order == 1:
        print("How many do you want?")
        piece = int(input("Piece"))
        price1 = Order1 * piece
        print ("Totals", price1, "THB")
    elif Order == 2:
        print("How many do you want?")
        piece = int(input("Piece"))
        price2 = Order2 * piece
        print ("Totals", price2, "THB")
    elif Order == 3:
        print("How many do you want?")
        piece = int(input("Piece"))
        price3 = Order3 * piece
        print ("Totals", price3, "THB")
    elif Order == 4:
        print("How many do you want?")
        piece = int(input("Piece"))
        price4 = Order4 * piece
        print("Totals", price4, "THB")
else:
    print("Login error")


