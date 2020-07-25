import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def addBrick():
    sql = "INSERT INTO Bricks (id, name, quantity, price) VALUES (%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    name=input("name:")
    quantity=input("quantity:")
    price=input("price(0000.00):")
    val=(str("%05d"%id),name,quantity,price)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute("SELECT *FROM Bricks WHERE id="+str("%05d"%id))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print(mycursor.rowcount,"record inserted.\n")
