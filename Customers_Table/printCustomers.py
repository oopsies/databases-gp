
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def printCustomers():
    print("1. All Customers")
    print("2. Specific Customer(s)")
    choice=int(input("Option:"))

    if choice == 1:
        customers_data = "SELECT * FROM Customers"
    elif choice == 2:
        customers_data = "SELECT * FROM Customers WHERE "
        attr = input("What is the attribute you are searching for (ex. name, address, phone)? ")
        val = "\'"+input(attr+"=")+"\'"
        record = attr+"="+val
        customers_data=customers_data+record
    else:
        print("Invalid Choice")
        printCustomers()
    mycursor.execute(customers_data)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)