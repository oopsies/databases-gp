import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def deleteEmployee():
    sql = "DELETE FROM Employees WHERE "
    attr = input("Delete using desired attribute(ex. name, id, store_preference):")
    val = "\'"+input(attr+"=")+"\'"
    record=attr+"="+val
    record=sql+record
    print(record)
    mycursor.execute(record)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted\n")
deleteEmployee()