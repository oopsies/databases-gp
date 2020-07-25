import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def addEmployee():
    id = random.randint(00000,99999)
    pin = random.randint(0000,9999)
    name=input("name:")
    store_preference=input("store_preference:")
    manage=input("manager(1 or 0):")
    sql="INSERT INTO Employees (id,name,store_preference,pin,manage) VALUES (%s,%s,%s,%s,%s)"
    val=(str("%05d"%id),name,store_preference,str("%04d"%pin),str(manage))
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute("SELECT *FROM Employees WHERE id="+str("%05d"%id))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print(mycursor.rowcount,"record inserted.\n")
