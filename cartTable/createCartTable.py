import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def createCartTable():
    sql = "CREATE TABLE Cart(itemID VARCHAR(5) NOT NULL,"\
        "cartID VARCHAR(5) NOT NULL,"\
        "user VARCHAR(255) DEFAULT 'GUEST',"\
        "itemQuantity INT UNSIGNED NOT NULL,"\
        "itemPrice DECIMAL (9,2) UNSIGNED,"\
        "itemCategory INT,"\
        "PRIMARY KEY(itemID,cartID,itemCategory))"
    mycursor.execute(sql)
createCartTable()
mycursor.execute("DESCRIBE Cart")
for x in mycursor:
    print(x)