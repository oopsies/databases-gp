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
    sql = "CREATE TABLE Payment (billing_address VARCHAR(255), " \
                                "card_type VARCHAR(32), " \
                                "card_number VARCHAR(16)," \
                                "user VARCHAR(255),"\
                                "PRIMARY KEY(billing_address,card_number))"
    mycursor.execute(sql)


createPaymentTable()
mycursor.execute("DESCRIBE Payment")
for x in mycursor:
    print(x)
