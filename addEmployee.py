import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def addEmployee():
    name=input("name:")
    store_preference=input("store_preference:")
    sql="INSERT INTO employees (name,store_preference) VALUES (%s,%s)"
    val=(name,store_preference)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")

addEmployee()
