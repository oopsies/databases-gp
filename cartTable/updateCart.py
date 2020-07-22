import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "tester",
    password = "tester",
    database = "LegoStore"
)

mycursor = mydb.cursor()

def updateCart():
    cartID=input("Desired CartID:")
    mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print("This Cart does not exist")
        updateCart()
    else:
        for x in myresult:
            print(x)
        itemID=input("Desired itemID:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("This item does not exist")
            updateCart()
        else:
            print("You are only allowed to change the amount")
            itemQuantity=input("How much of this item do you want?\nOption:")
            if int(itemQuantity) == 0:
                mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
                myresult = mycursor.fetchall()
                mycursor.execute("DELETE FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
                mydb.commit()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) deleted\n")
            elif int(itemQuantity) > 0:
                mycursor.execute("UPDATE Cart SET itemQuantity="+itemQuantity+" WHERE cartID="+cartID+" AND itemID="+itemID)
                mydb.commit()
                mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) affected\n")
            else:
                print("Invalid Amount")
                updateCart()

