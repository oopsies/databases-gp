import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def createSaleTable():
    sql = "CREATE TABLE Sale (cartID VARCHAR(5) NOT NULL,"\
        "saleDate date NOT NULL,"\
        "price DECIMAL (9,2) UNSIGNED,"\
        "PRIMARY KEY(cartID,saleDate))"
    mycursor.execute(sql)
    mycursor.execute("DESCRIBE Sale")
    for x in mycursor:
        print(x)
createSaleTable()