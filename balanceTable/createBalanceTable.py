import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createBalanceTable():
    sql = "CREATE TABLE Balance(cartID VARCHAR(5) PRIMARY KEY, price DECIMAL (9,2) UNSIGNED)"
    mycursor.execute(sql)
    mycursor.execute("DESCRIBE Balance")
    for x in mycursor:
        print(x)
createBalanceTable()
