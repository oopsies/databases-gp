import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()
def printFromCart(user):
    if user == "":
        user="Guest"
    mycursor.execute("SELECT Cart.itemID, Cart.cartID, Cart.user, Cart.itemQuantity, Cart.itemPrice, Cart.itemCategory FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Cart.user=\'"+user+"\' AND Balance.price!=0")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)





def printCart():
    print("1.Print All Carts")
    print("2.Print Cart")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT DISTINCT Cart.cartID FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    elif choice == 2:
        mycursor.execute("SELECT DISTINCT cartID FROM Cart")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        cartID=input("cartID:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("Invalid ID")
            printCart()
        else:
            for x in myresult:
                print(x)
            mycursor.execute("SELECT *FROM Balance WHERE cartID="+cartID)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        
