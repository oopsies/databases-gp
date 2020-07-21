import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def addCustomers():
    name = input('name: ')
	email = input('email: ')
    address = input('email: ')
	phone = input('phone: ')
    customers_data="INSERT INTO Employees (name, email, address, phone) VALUES (%s,%s,%s,%s)"
    val=(name, email, address, str(phone))
    mycursor.execute(customers_data,val)
    mydb.commit()
    
    print(mycursor.rowcount,"record inserted.\n")

addCustomers()