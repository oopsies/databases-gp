import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def printSale():
    print("1. All Sales")
    print("2. By id")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT *FROM Sale")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
    if choice == 2:
        mycursor.execute("SELECT *FROM Sale")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        cartID=input("ID:")
        mycursor.execute("SELECT Cart.itemID,Cart.itemQuantity,Cart.itemPrice,Cart.user FROM Sale RIGHT JOIN Cart ON Cart.cartID=Sale.cartID WHERE Sale.cartID="+cartID)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)