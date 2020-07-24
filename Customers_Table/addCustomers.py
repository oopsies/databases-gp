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
    address = input('address: ')
    phone = input('phone: ')
    customers_data="INSERT INTO Customers (name, email, address, phone) VALUES (%s,%s,%s,%s)"
    val=(name, email, address, str(phone))
    mycursor.execute(customers_data,val)
    mydb.commit()
    
    print(mycursor.rowcount,"record inserted.\n")
