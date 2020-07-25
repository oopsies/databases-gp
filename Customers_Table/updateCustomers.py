import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def updateCustomers():
    customers_data = "UPDATE Customers SET "
    newAttr = input("What value would you like to change(name, email, address, phone,password)?")
    newVal = "\'"+input("What value do you want?\n"+newAttr+"=")+"\'"
    targetAttr = input("Which attributes are you searching for(name, email, address, phone)?")
    targetVal = "\'"+input("What value does it have?\n"+targetAttr+"=")+"\'"
    customers_data = customers_data + newAttr +"="+newVal+" WHERE "+targetAttr+"="+targetVal
    print(customers_data)
    mycursor.execute(customers_data)
    mydb.commit()
    
    print(mycursor.rowcount,"record(s) affected\n")
updateCustomers()
