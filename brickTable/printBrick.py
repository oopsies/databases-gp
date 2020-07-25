import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def printBrick():
    print("1. All Bricks")
    print("2. Specific Brick(s)")
    choice=int(input("Option:"))

    if choice == 1:
        sql = "SELECT * FROM Bricks"
    elif choice == 2:
        sql = "SELECT * FROM Bricks WHERE "
        attr = input("What is the attribute you are searching for (ex. id, name, quantity, price)?")
        val = "\'"+input(attr+"=")+"\'"
        record = attr+"="+val
        sql=sql+record
    else:
        print("Invalid Choice")
        printBrick()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

