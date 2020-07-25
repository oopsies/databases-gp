import mysql.connector, decimal
from datetime import date
mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()
name=""
def payOnlineCart(user):
    if user == "":
        user="Guest"
    mycursor.execute("SELECT Cart.itemID, Cart.cartID, Cart.itemQuantity, Cart.itemPrice  FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE user=\'"+user+"\' AND Balance.price!=0")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    if user == "Guest":
        mycursor.execute("SELECT Balance.price FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE user=\'"+user+"\' AND Balance.price!=0")
        myresult = mycursor.fetchall()
        for x in myresult:
            price=x[0]
            print(str(x[0]))
        cardNumber=input("CardNumber:")
        if len(cardNumber) != 16:
            print("Invalid Number")
            payOnlineCart(user)
        else:
            card_type=input("Type:")
            billing_address=input("Input Billing Address:")
            delivery_address=input("Delivery Address:")
            sql = "INSERT INTO Payment(billing_address,card_type,card_number,user) VALUES (%s,%s,%s)"
            entry = (billing_address,card_type,cardNumber,user)
            mycursor.execute(sql,entry)
        
payOnlineCart(name)


def payCart():
    mycursor.execute("SELECT DISTINCT Cart.cartID FROM Cart RIGHT JOIN Balance ON Cart.cartID=Balance.cartID WHERE Balance.price!=0")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    cartID=input("Insert CartID:")
    mycursor.execute("SELECT SUM(itemQuantity*itemPrice) FROM Cart WHERE cartID="+cartID)
    myresult = mycursor.fetchall()
    saleCost=myresult[0][0]
    mycursor.execute("SELECT *FROM Cart WHERE cartID="+cartID)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print("Invalid CartID")
        payCart()
    else:
        for x in myresult:
            print(x)
        mycursor.execute("SELECT price FROM Balance WHERE cartID="+cartID)
        myresult = mycursor.fetchall()
        for x in myresult:
            price=x[0]
            print("Balance="+str(x[0]))

        payMethod=input("Cash or Card:")
        if payMethod in ['cash','Cash']:
            amount=float(input("Payment Amount:"))
            amount=decimal.Decimal(amount)
            if amount>price:
                newBal=0
                print("Change Owed="+str(amount-price))
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()

                mycursor.execute("SELECT price FROM Balance WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) affected\n")

                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                
            elif amount<price:
                newBal=price-amount
                print("Remaining Price="+str(newBal))
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
            elif amount==price:
                newBal=0
                print("No Change Owed")
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
        elif payMethod in ['card','Card']:
            cardNumber=input("card:")
            if len(cardNumber) != 16:
                print("Invalid Card Number")
                payCart()
            else:
                amount=float(input("Payment Amount:"))
                amount=decimal.Decimal(amount)
            if amount>price:
                newBal=0
                print("Change Owed="+str(amount-price))
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()

                mycursor.execute("SELECT price FROM Balance WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) affected\n")

                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                
            elif amount<price:
                newBal=price-amount
                print("Remaining Price="+str(newBal))
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
            elif amount==price:
                newBal=0
                print("No Change Owed")
                sql="UPDATE Balance SET price="+str(newBal)+" WHERE cartID="+cartID
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute("SELECT price FROM Sale WHERE cartID="+cartID)
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    sql="INSERT INTO Sale (cartID,saleDate,price) VALUES (%s,%s,%s)"
                    entry=(cartID,str(date.today()),str(saleCost))
                    price=0
                    mycursor.execute(sql,entry)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                else:
                    price=myresult[0][0]+price    
                    sql="UPDATE Sale SET price="+str(saleCost)+" WHERE cartID="+cartID
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("SELECT *FROM Sale WHERE cartID="+cartID)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)