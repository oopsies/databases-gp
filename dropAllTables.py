import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()


print("DROPPED BRICKS\n")
mycursor.execute("DROP TABLE Bricks")
print("DROPPED BALANCE\n")
mycursor.execute("DROP TABLE Balance")
print("DROPPED CART\n")
mycursor.execute("DROP TABLE Cart")
print("DROPPED SALE\n")
mycursor.execute("DROP TABLE Sale")
print("DROPPED SET_T\n")
mycursor.execute("DROP TABLE Set_t")
print("DROPPED CUSTOMERS\n")
mycursor.execute("DROP TABLE Customers")
print("DROPPED EMPLOYEES\n")
mycursor.execute("DROP TABLE Employees")
print("DROPPED PAYMENT\n")
mycursor.execute("DROP TABLE Payment")