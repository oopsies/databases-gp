import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def deleteCart():
    print("1. Delete whole Cart")
    print("2. Delete item from Cart")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT DISTINCT cartID, user FROM Cart")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        cartID=input("Insert CartID you want deleted:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("Invalid Cart ID")
            deleteCart()
        else:
            mycursor.execute("DELETE FROM Cart Where cartID="+cartID)
            mydb.commit()
            for x in myresult:
                print(x)
            print(mycursor.rowcount,"record(s) deleted\n")
    if choice == 2:
        mycursor.execute("SELECT DISTINCT cartID, user FROM CART")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        cartID=input("Insert CartID:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("Invalid Cart ID")
            deleteCart()
        else:
            for x in myresult:
                print(x)
            itemID=input("ItemID you want to drop:")
            mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("Invalid Item ID")
                deleteCart()
            else:
                mycursor.execute("DELETE FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
                mydb.commit()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) deleted\n")
            