import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def testInserts():
    sql="INSERT INTO Cart(itemID, cartID, user, itemQuantity, itemPrice, itemCategory) VALUES (%s,%s,%s,%s,%s,%s)"
    itemID=random.randint(00000,99999)
    cartID=random.randint(00000,99999)
    entry=(str("%05d"%itemID),str("%05d"%cartID),"GUEST","2","49.99","0")
    entry2=(str("%05d"%(itemID+1)),str("%05d"%cartID),"GUEST","2","79.99","1")
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mydb.commit()
    mycursor.execute("SELECT *FROM Cart")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
testInserts()