import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createSaleTable():
    sql = "CREATE TABLE Sale (itemID VARCHAR(5) NOT NULL,"\
        "store VARCHAR(255) NOT NULL,"\
        "quantity INT UNSIGNED NOT NULL,"\
        "saleDate date NOT NULL,"\
        "itemCategory INT,"\
        "price DECIMAL (9,2) UNSIGNED,"\
        "PRIMARY KEY(itemID,itemCategory,saleDate))"
    mycursor.execute(sql)
    mycursor.execute("DESCRIBE Sale")
    for x in mycursor:
        print(x)
createSaleTable()