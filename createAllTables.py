import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()
print("EMPLOYEES TABLE")
def createEmployeesTable():
    sql = "CREATE TABLE Employees (id VARCHAR(5) NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, store_preference VARCHAR(255) NOT NULL, pin VARCHAR(5) NOT NULL, manage INT NOT NULL )"
    mycursor.execute(sql)

createEmployeesTable()
mycursor.execute("DESCRIBE Employees")
for x in mycursor:
    print(x)
print("\n\n")

print("CUSTOMERS TABLE")
def createCustomersTable():
    customers_data = "CREATE TABLE Customers (name VARCHAR(100) NOT NULL, email VARCHAR (100) NOT NULL PRIMARY KEY, address VARCHAR(150) NOT NULL, phone VARCHAR(20), password VARCHAR(20))"
    mycursor.execute(customers_data)

createCustomersTable() #Error if ON
mycursor.execute("DESCRIBE Customers")
for x in mycursor:
    print(x)
print("\n\n")

print("PAYMENT TABLE")
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
print("\n\n")

print("SALE TABLE")
def createSaleTable():
    sql = "CREATE TABLE Sale (cartID VARCHAR(5) NOT NULL,"\
        "saleDate date NOT NULL,"\
        "price DECIMAL (9,2) UNSIGNED,"\
        "delivery_address VARCHAR(255) DEFAULT 'NONE',"\
        "delivery_date date,"\
        "PRIMARY KEY(cartID,saleDate))"
    mycursor.execute(sql)
    mycursor.execute("DESCRIBE Sale")
    for x in mycursor:
        print(x)
createSaleTable()
print("\n\n")

print("SET TABLE")
def createSetTable():
    sql = "CREATE TABLE Set_t (set_id VARCHAR(5) NOT NULL,"\
          "name VARCHAR(255) NOT NULL,"\
          "brick_id VARCHAR(5) NOT NULL,"\
          "bricks_needed INT NOT NULL,"\
          "PRIMARY KEY (set_id,brick_id))"
    mycursor.execute(sql)
createSetTable()
mycursor.execute("DESCRIBE Set_t")
for x in mycursor:
    print(x)
print("\n\n")

print("BALANCE TABLE")
def createBalanceTable():
    sql = "CREATE TABLE Balance(cartID VARCHAR(5) PRIMARY KEY, price DECIMAL (9,2) UNSIGNED)"
    mycursor.execute(sql)
    mycursor.execute("DESCRIBE Balance")
    for x in mycursor:
        print(x)
createBalanceTable()
print("\n\n")

print("BRICKS TABLE")
def createBricksTable():
    sql = "CREATE TABLE Bricks (id VARCHAR(5) PRIMARY KEY, name VARCHAR(255), quantity INT UNSIGNED, price DECIMAL (6,2) UNSIGNED)"
    mycursor.execute(sql)
createBricksTable()
mycursor.execute("DESCRIBE Bricks")
for x in mycursor:
    print(x)
print("\n\n")

print("CART TABLE")
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
print("\n\n")