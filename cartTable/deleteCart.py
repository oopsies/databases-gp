import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

name=""
def deleteFromCart(user):
    print("1.Delete whole Cart")
    print("2.Delete item from Cart")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("DELETE Cart FROM Cart INNER JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0 AND user=\'"+user+"\'")
        mydb.commit()
    elif choice == 2:
        mycursor.execute("SELECT *FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0 AND user=\'"+user+"\'")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        itemID=input("itemID:")
        mycursor.execute("SELECT *FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0 AND user=\'"+user+"\' AND itemID="+itemID)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        mycursor.execute("DELETE Cart FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0 AND user=\'"+user+"\' AND itemID="+itemID)
        mydb.commit()
        print(mycursor.rowcount,"record(s) deleted\n")

def returnSale():
    print("1. Whole Cart")
    print("2. Single Item")
    choice=int(input("Option:"))

    if choice == 1:
        cartID=input("CartID:")
        mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
        myresult=mycursor.fetchall()
        if len(myresult) == 0:
            print("No record of that Sale")
        else:
            mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
            myres=mycursor.fetchall()
            for x in myres:
                print(x)
            for x in myresult:
                print(x)
            mycursor.execute("DELETE FROM Sale WHERE cartID="+cartID)
            mydb.commit()
            mycursor.execute("DELETE FROM Cart WHERE cartID="+cartID)
            mydb.commit()
    elif choice == 2:
        cartID=input("CartID:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("No record of that Sale")
        else:
            for x in myresult:
                print(x)
            itemID=input("Item you would like to return\nitemID:")
            mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
            myres= mycursor.fetchall()
            for x in myres:
                print(str(x[0])+" owed")
            mycursor.execute("DELETE FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
            mydb.commit()
            mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
            myresult = mycursor.fetchall()
            newSale=myresult[0][0]
            mycursor.execute("UPDATE Sale SET price="+str(newSale)+" WHERE cartID="+cartID)
            mydb.commit()
            mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
            myres = mycursor.fetchall()
            for x in myres:
                print(x)

def returnOnlineOrder(user):
    if user == "":
        user="Guest"
    mycursor.execute("SELECT *FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Cart.user=\'"+user+"\' AND Balance.price=0")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    cartID=input("Insert CartID:")
    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
    myresult=mycursor.fetchall()
    if len(myresult) == 0:
        print("No record of this sale")
    else:
        itemID=input("Insert ItemID:")
        mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID+" AND itemID="+itemID)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("Item Does not exist in Cart")
        else:
            for x in myresult:
                refund=x[0]
            print("Refund="+str(refund))
            mycursor.execute("DELETE FROM Cart WHERE Cart.cartID="+cartID+" AND Cart.itemID="+itemID)
            mydb.commit()
            mycursor.execute("SELECT *FROM Cart WHERE Cart.cartID="+cartID)
            myres = mycursor.fetchall()
            mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
            myresult = mycursor.fetchall()
            newSale=myresult[0][0]
            if len(myres) == 0:
                mycursor.execute("DELETE FROM Sale WHERE cartID="+cartID)
            else:
                mycursor.execute("UPDATE Sale SET price="+str(newSale)+" WHERE cartID="+cartID)
                mydb.commit()
                mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)

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
            mycursor.execute("DELETE FROM Cart WHERE cartID="+cartID)
            mydb.commit()
            for x in myresult:
                print(x)
            print(mycursor.rowcount,"record(s) deleted\n")
            mycursor.execute("DELETE FROM Balance WHERE cartID="+cartID)
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

                mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
                myresult=mycursor.fetchall()
                if len(myresult) == 0:
                    mycursor.execute("DELETE FROM Balance WHERE cartID="+cartID)
                    mydb.commit()
                    print(mycursor.rowcount,"record(s) deleted\n")
                else:
                    for x in myresult:
                        price=x[0]
                    sql="UPDATE Balance SET price="+str(price)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()

                    mycursor.execute("SELECT *FROM Balance WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                    print(mycursor.rowcount,"record(s) affected\n")
            
