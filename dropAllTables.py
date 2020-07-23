import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE Bricks")
mycursor.execute("DROP TABLE Balance")
mycursor.execute("DROP TABLE Cart")
mycursor.execute("DROP TABLE Sales")
mycursor.execute("DROP TABLE Set_t")
mycursor.execute("DROP TABLE Customers")
mycursor.execute("DROP TABLE Employees")
mycursor.execute("DROP TABLE Payment")