#Create table for payments
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createPaymentTable():
    sql = "CREATE TABLE Payment (payment_type VARCHAR(4) NOT NULL, " \
                                "billing_address VARCHAR(255) PRIMARY KEY, " \
                                "card_type VARCHAR(32), " \
                                "card_number VARCHAR(16)," \
                                "amount DECIMAL(6, 2) NOT NULL)"
    mycursor.execute(sql)


createPaymentTable()
mycursor.execute("DESCRIBE Payment")
for x in mycursor:
    print(x)
