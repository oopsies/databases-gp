import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def addCart():
    print("1.Create New Cart")
    print("2.Add to existing Cart")
    choice=int(input("Option:"))

    if choice == 1:
        sql = "INSERT INTO Cart(itemID, cartID, user, itemQuantity, itemPrice, itemCategory) VALUES (%s,%s,%s,%s,%s,%s) "
        cartID=random.randint(00000,99999)
        item=input("Set or Brick:")
        if item in ['set','Set']:
            print("Set")
            set_id=input("SetID:")
            mycursor.execute("SELECT SUM(bricks_needed*price) FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("The Set Does not Exist")
                addCart()
            else:
                user="GUEST"
                itemQuantity=input("How much of the following item do you want?\n")
                price=myresult[0][0]
                entry=(set_id,str("%05d"%cartID),user,str(itemQuantity),str(price),"1")
                mycursor.execute(sql,entry)
                mydb.commit()
                mycursor.execute("SELECT *FROM Cart WHERE cartID="+str("%05d"%cartID))
                myresult = mycursor.fetchall()
                for x in myresult:
                   print(x)
                print(mycursor.rowcount,"record inserted.\n")

                mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+str("%05d"%cartID))
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=x[0]

                sql="INSERT INTO Balance(cartID,price) VALUES (%s,%s)"
                val=(str("%05d"%cartID),str(price))
                mycursor.execute(sql,val)
                mydb.commit()
                mycursor.execute("SELECT *FROM Balance")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)


        elif item in ['brick','Brick']:
            print("Brick")
            brick_id=input("BrickID:")
            mycursor.execute("SELECT price FROM Bricks WHERE id="+brick_id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("This Brick Does not Exist")
                addCart()
            else:
                user="GUEST"
                itemQuantity=input("How much of the following item do you want?\n")
                price=myresult[0][0]
                entry=(brick_id,str("%05d"%cartID),user,str(itemQuantity),str(price),"0")
                mycursor.execute(sql,entry)
                mydb.commit()
                mycursor.execute("SELECT *FROM Cart WHERE cartID="+str("%05d"%cartID))
                myresult = mycursor.fetchall()
                for x in myresult:
                   print(x)
                print(mycursor.rowcount,"record inserted.\n")

                mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+str("%05d"%cartID))
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=x[0]

                sql="INSERT INTO Balance(cartID,price) VALUES (%s,%s)"
                val=(str("%05d"%cartID),str(price))
                mycursor.execute(sql,val)
                mydb.commit()
                mycursor.execute("SELECT *FROM Balance")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
    
    elif choice == 2:
        sql = "INSERT INTO Cart(itemID, cartID, user, itemQuantity, itemPrice, itemCategory) VALUES (%s,%s,%s,%s,%s,%s) "
        mycursor.execute("SELECT DISTINCT cartID FROM Cart")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        cartID=input("CartID:")
        mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
        myresult=mycursor.fetchall()
        if len(myresult) == 0:
            print("This Cart Does not Exist")
            addCart()
        else:
            for x in myresult:
                print(x)
            item=input("Set or Brick:")
            if item in ['set','Set']:
                print("Set")
                set_id=input("SetID:")
                mycursor.execute("SELECT SUM(bricks_needed*price) FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    print("The Set Does not Exist")
                    addCart()
                else:
                    user="GUEST"
                    itemQuantity=input("How much of the following item do you want?\n")
                    price=myresult[0][0]
                    entry=(set_id,cartID,user,str(itemQuantity),str(price),"1")
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                    print(mycursor.rowcount,"record inserted.\n")

                    mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
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

            elif item in ['brick','Brick']:
                print("Brick")
                brick_id=input("BrickID:")
                mycursor.execute("SELECT price FROM Bricks WHERE id="+brick_id)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    print("This Brick Does not Exist")
                    addCart()
                else:
                    user="GUEST"
                    itemQuantity=input("How much of the following item do you want?\n")
                    price=myresult[0][0]
                    entry=(brick_id,cartID,user,str(itemQuantity),str(price),"0")
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                      print(x)
                    print(mycursor.rowcount,"record inserted.\n")  

                    mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
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