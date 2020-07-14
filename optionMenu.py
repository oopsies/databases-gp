
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def storeLogin():
    attempts=0
    accessStatus=0
    for x in range(4):
        user="\'"+input("username:")+"\'"
        password="\'"+input("password:")+"\'"
        sql="SELECT * FROM Employees WHERE id="+user+" AND pin="+password
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        y=len(myresult)
        if y == 0:
            print("Incorrect Password/Username Try Again")
            attempts+=1
        else:
            print("Access Granted")
            for i in myresult:
                print(i)
            accessStatus=1
            break
    if attempts==4:
        print("Too many incorrect guesses")
    return accessStatus

def employee():
    choice=0
    while choice!=5:
        print("1. Add Employee(s)")
        print("2. Update Employee(s)")
        print("3. Delete Employee(s)")
        print("4. Print Employee(s)")
        print("5. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print("Add Employee")
            from employeeTable import addEmployee
        if choice == 2:
            print("Update Employee")
            from employeeTable import updateEmployee
        if choice == 3:
            print("Delete Employee")
            from employeeTable import deleteEmployee
        if choice == 4:
            print("Print Employee")
            from employeeTable import printEmployee


def storeMode():
    choice=0
    while choice!=6:
        print("1. Employee Management")
        print("2. Order Management")
        print("3. Reports")
        print("4. Search Item")
        print ("5. Payment")
        print("6. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print ("Employee Management\n")
            employee()
        if choice == 2:
            print ("Order Management\n")
        if choice == 3:
            print ("Reports\n")
        if choice == 4:
            print ("Search Item\n")
        if choice == 5:
            print ("Payment\n")

def menu():
    choice=0
    while choice!=3:
        print("1. Store Mode")
        print("2. Online Mode")
        print("3. Quit")
        choice=int(input("Option:"))
        if choice == 1:
            print("Store mode selected\n")
            res=storeLogin()
            if res == 1:
                storeMode()
        if choice == 2:
            print("Online mode selected\n")
menu()