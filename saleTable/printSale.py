import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()
name = ""
def printSaleHistory(user):
    if user == "":
        user="Guest"
    mycursor.execute("SELECT DISTINCT Cart.cartID, Sale.saleDate, Sale.price, Sale.delivery_address, Sale.delivery_date FROM Sale RIGHT JOIN Cart ON Cart.cartID=Sale.cartID WHERE Cart.user=\'"+user+"\'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    cartID=input("Insert CartID to see further details\nID:")
    mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

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