import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def testInserts():
    sql = "INSERT INTO Employees (id,name,store_preference,pin,manage) VALUES (%s,%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    id2 = random.randint(00000,99999)
    id3 = random.randint(00000,99999)
    pin = random.randint(0000,9999)
    pin2 = random.randint(0000,9999)
    pin3 = random.randint(0000,9999)
    entry = (str("%05d"%id),"Khaemon Edwards", "Denton",str("%04d"%pin),"0")
    entry2 = (str("%05d"%id2),"Reynaldo Ferrari", "Denton", str("%04d"%pin2),"1")
    entry3 = (str("%05d"%id3),"Ryan Vanek", "Denton", str("%04d"%pin3),"1")
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mycursor.execute(sql,entry3)
    mydb.commit()
    mycursor.execute("SELECT *FROM Employees")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
testInserts()