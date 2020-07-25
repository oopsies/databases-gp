#Create table for reports
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createPaymentTable():
    sql = "CREATE TABLE Report (report_id VARCHAR(255) NOT NULL PRIMARY KEY," \
                                "brick_id VARCHAR(5)," \
                                "quantity INT UNSIGNED," \
                                "price DECIMAL (6,2) UNSIGNED," \
                                "data VARCHAR(255))"
    mycursor.execute(sql)


createPaymentTable()
mycursor.execute("DESCRIBE Payment")
for x in mycursor:
    print(x)
