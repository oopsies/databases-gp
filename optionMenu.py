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
            from employeesTable import addEmployee
        elif choice == 2:
            print("Update Employee")
            from employeesTable import updateEmployee
        elif choice == 3:
            print("Delete Employee")
            from employeesTable import deleteEmployee
        elif choice == 4:
            print("Print Employee")
            from employeesTable import printEmployee


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
        elif choice == 2:
            print ("Order Management\n")
        elif choice == 3:
            print ("Reports\n")
        elif choice == 4:
            print ("Search Item\n")
        elif choice == 5:
            print ("Payment\n")

def onlineMode():
    choice=0
    while choice!=6:
        print("1. Add to Cart")
        print("2. Browse Sets/Bricks")
        print("3. View Cart")
        print("4. View History")
        print("5. Pay for Cart")
        print("6. Back")
        choice = int(input("Option:"))

        if choice == 1:
            print("Add to Cart\n")
        elif choice == 2:
            print("Browse Sets/Bricks\n")
        elif choice == 3:
            print("View Cart\n")
        elif choice == 4:
            print("View History\n")
        elif choice == 5:
            print("Pay for cart\n")



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
        elif choice == 2:
            print("Online mode selected\n")
            onlineMode()
menu()