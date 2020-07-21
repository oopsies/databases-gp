import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def printEmployee():
    print("1. All Employees")
    print("2. Specific Employee(s)")
    choice=int(input("Option:"))

    if choice == 1:
        sql = "SELECT * FROM employees"
    elif choice == 2:
        sql = "SELECT * FROM employees WHERE "
        attr = input("What is the attribute you are searching for (ex. id, name, store_preference)?")
        val = "\'"+input(attr+"=")+"\'"
        record = attr+"="+val
        sql=sql+record
    else:
        print("Invalid Choice")
        printEmployee()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
