import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def deleteBrick():
    sql = "DELETE FROM Bricks WHERE "
    attr = input("Delete using desired attribute(ex. id, name, quantity, price):")
    val = "\'"+input(attr+"=")+"\'"
    record=attr+"="+val
    record=sql+record
    mycursor.execute("SELECT *FROM Bricks WHERE "+attr+"="+val)
    myresult = mycursor.fetchall()
    mycursor.execute(record)
    mydb.commit()
    for x in myresult:
        print(x)
    print(mycursor.rowcount,"record(s) deleted\n")
