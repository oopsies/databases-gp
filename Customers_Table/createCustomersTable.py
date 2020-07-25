import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore", #delete line if error appears
    autocommit=True
)

mycursor = mydb.cursor() #AWAYS ON

def createCustomersTable():
    customers_data = "CREATE TABLE Customers (name VARCHAR(100) NOT NULL, email VARCHAR (100) NOT NULL PRIMARY KEY, address VARCHAR(150) NOT NULL, phone VARCHAR(20), password VARCHAR(20))"
    mycursor.execute(customers_data)

createCustomersTable() #Error if ON
mycursor.execute("DESCRIBE Customers")
for x in mycursor:
    print(x)
