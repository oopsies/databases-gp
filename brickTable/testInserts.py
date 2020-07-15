import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def testInserts():
    sql = "INSERT INTO Bricks (id, name, quantity, price) VALUES (%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    id2 = random.randint(00000,99999)
    id3 = random.randint(00000,99999)
    price = random.uniform(000.00,999.99)
    price2 = random.uniform(000.00,999.99)
    price3 = random.uniform(000.00,999.99)
    entry = (str("%05d"%id),"1x1 Golden Torso", "7", price)
    entry2 = (str("%05d"%id2),"1x1 Golden Leg", "7", price2)
    entry3 = (str("%05d"%id3),"1x1 Golden Head", "7", price3)
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mycursor.execute(sql,entry3)
    mydb.commit()
    mycursor.execute("SELECT *FROM Bricks")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
testInserts()