import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def printCart():
    print("1.Print All Carts")
    print("2.Print Cart")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT DISTINCT cartID FROM Cart")
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
        
