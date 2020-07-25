import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def deleteCustomers():
    customers_data = "DELETE FROM Customers WHERE "
    attr = input("Delete using desired attribute(ex. name, address, email, phone): ")
    val = "\'"+input(attr+"=")+"\'"
    record=attr+"="+val
    record=customers_data+record
    mycursor.execute("SELECT *FROM Customers WHERE "+attr+"="+val)
    myresult = mycursor.fetchall()
    mycursor.execute(record)
    mydb.commit()
    for x in myresult:
        print(x)
    print(mycursor.rowcount,"record(s) deleted\n")