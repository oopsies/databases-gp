import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createBricksTable():
    sql = "CREATE TABLE Bricks (id VARCHAR(5) PRIMARY KEY, name VARCHAR(255), quantity INT UNSIGNED, price DECIMAL (6,2) UNSIGNED)"
    mycursor.execute(sql)
createBricksTable()