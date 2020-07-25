import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def testInserts():
    print("EMPLOYEES")
    sql = "INSERT INTO Employees (id,name,store_preference,pin,manage) VALUES (%s,%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    id2 = random.randint(00000,99999)
    id3 = random.randint(00000,99999)
    pin = random.randint(0000,9999)
    pin2 = random.randint(0000,9999)
    pin3 = random.randint(0000,9999)
    entry = (str("%05d"%id),"Regular Employee", "Denton",str("%04d"%pin),"0")
    entry2 = (str("%05d"%id2),"Manager Employee", "Denton", str("%04d"%pin2),"1")
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mydb.commit()
    mycursor.execute("SELECT *FROM Employees")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("\n\n")
    
    print("BRICKS")
    sql = "INSERT INTO Bricks (id, name, quantity, price) VALUES (%s,%s,%s,%s) "
    bid = random.randint(00000,99999)
    bid2 = random.randint(00000,99999)
    bid3 = random.randint(00000,99999)
    price = random.uniform(00.00,99.99)
    price2 = random.uniform(00.00,99.99)
    price3 = random.uniform(00.00,99.99)
    entry = (str("%05d"%bid),"1x1 Golden Torso", "7", price)
    entry2 = (str("%05d"%bid2),"1x1 Golden Leg", "77", price2)
    entry3 = (str("%05d"%bid3),"1x1 Golden Head", "777", price3)
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mycursor.execute(sql,entry3)
    mydb.commit()
    mycursor.execute("SELECT *FROM Bricks")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("\n\n")

    print("SETS")
    sql="INSERT INTO Set_t(set_id, name, brick_id, bricks_needed) VALUES (%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    entry=(str("%05d"%id),"Golden Combo",str("%05d"%bid),"1")
    entry2=(str("%05d"%id),"Golden Combo",str("%05d"%bid2),"1")
    entry3=(str("%05d"%id),"Golden Combo",str("%05d"%bid3),"2")
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mycursor.execute(sql,entry3)
    mydb.commit()
    mycursor.execute("SELECT DISTINCT set_id,name,brick_id FROM Set_t")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("\n\n")

    print("CUSTOMERS")
    sql="INSERT INTO Customers(name,email,address,phone,password) VALUES (%s,%s,%s,%s,%s)"
    entry=("Online Shopper","tester@email.com","Amazing Spot Denton","8880009999","password")
    mycursor.execute(sql,entry)
    mydb.commit()
    mycursor.execute("SELECT *FROM Customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("\n\n")
testInserts()