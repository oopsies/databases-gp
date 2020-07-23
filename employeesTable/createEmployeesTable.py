import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createEmployeesTable():
    sql = "CREATE TABLE Employees (id VARCHAR(5) NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, store_preference VARCHAR(255) NOT NULL, pin VARCHAR(5) NOT NULL )"
    mycursor.execute(sql)

createEmployeesTable()
mycursor.execute("DESCRIBE Employees")
for x in mycursor:
    print(x)