import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()
username="none"
def storeLogin():
    attempts=0
    accessStatus=0
    for x in range(4):
        user="\'"+input("username:")+"\'"
        password="\'"+input("password:")+"\'"
        sql="SELECT manage FROM Employees WHERE id="+user+" AND pin="+password
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        y=len(myresult)
        if y == 0:
            print("Incorrect Password/Username Try Again")
            attempts+=1
        else:
            print("Access Granted")
            for i in myresult:
                accessStatus=i[0]
            break
    if attempts==4:
        print("Too many incorrect guesses")
    username=user
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
            from employeesTable.addEmployee import addEmployee
            addEmployee()
        elif choice == 2:
            print("Update Employee")
            from employeesTable.updateEmployee import updateEmployee
            updateEmployee()
        elif choice == 3:
            print("Delete Employee")
            from employeesTable.deleteEmployee import deleteEmployee
            deleteEmployee()
        elif choice == 4:
            print("Print Employee")
            from employeesTable.printEmployee import printEmployee
            printEmployee()

def cart():
    choice=0
    while choice!=5:
        print("1. Add to Cart")
        print("2. Update Cart")
        print("3. Delete Cart")
        print("4. View Cart")
        print("5. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print("Add to Cart")
            from cartTable.addCart import addCart
            addCart()
        elif choice == 2:
            print("Update Cart")
            from cartTable.updateCart import updateCart
            updateCart()
        elif choice == 3:
            print("Delete Cart")
            from cartTable.deleteCart import deleteCart
            deleteCart()
        elif choice == 4:
            print("View Cart")
            from cartTable.printCart import printCart
            printCart()

def item():
    choice=0
    while choice!=9:
        print("1. Add Brick")
        print("2. Delete Brick(s)")
        print("3. Update Brick(s)")
        print("4. Print Brick(s)")
        print("5. Add Set")
        print("6. Delete Set(s)")
        print("7. Update Set(s)")
        print("8. Print Set(s)")
        print("9. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print("Add Brick")
            from brickTable.addBrick import addBrick
            addBrick()
        elif choice == 2:
            print("Delete Brick(s)")
            from brickTable.deleteBrick import deleteBrick
            deleteBrick()
        elif choice == 3:
            print("Update Brick(s)")
            from brickTable.updateBrick import updateBrick
            updateBrick()
        elif choice == 4:
            print("Print Brick(s)")
            from brickTable.printBrick import printBrick
            printBrick()
        elif choice == 5:
            print("Add Set")
            from setTable.addSet import addSet
            addSet()
        elif choice == 6:
            print("Delete Brick(s)")
            from setTable.deleteSet import deleteSet
            deleteSet()
        elif choice == 7:
            print("Update Set(s)")
            from setTable.updateSetTable import updateSet
            updateSet()
        elif choice == 8:
            print("Print Set(s)")
            from setTable.printSet import printSet
            printSet()
        elif choice != 9:
            print("Invalid Choice")

def storeMode():
    choice=0
    while choice!=6:
        print("1. Order Management")
        print("2. Reports")
        print("3. Item Management")
        print("4. Payment")
        print("5. Sale")
        print("6. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print ("Order Management\n")
            cart()
        elif choice == 2:
            print ("Reports\n")
        elif choice == 3:
            print ("Item Management\n")
            item()
        elif choice == 4:
            print ("Payment\n")
        elif choice == 5:
            print("Sale\n")
            cart()

def storeModeManager():
    choice=0
    while choice!=7:
        print("1. Employee Management")
        print("2. Order Management")
        print("3. Reports")
        print("4. Item Management")
        print("5. Payment")
        print("6. Sale")
        print("7. Back")
        choice=int(input("Option:"))
        if choice == 1:
            print ("Employee Management\n")
            employee()
        elif choice == 2:
            print ("Order Management\n")
            cart()
        elif choice == 3:
            print ("Reports\n")
        elif choice == 4:
            print ("Item Management\n")
            item()
        elif choice == 5:
            print ("Payment\n")
def onlineMode():
    choice=0
    while choice!=7:
        print("1. Add to Cart")
        print("2. Browse Sets")
        print("3. View Cart")
        print("4. View History")
        print("5. Pay for Cart")
        print("6. Browse Bricks")
        print("7. Back")
        choice = int(input("Option:"))

        if choice == 1:
            print("Add to Cart\n")
        elif choice == 2:
            print("Browse Sets\n")
            from setTable.printSet import printSet
            printSet()
        elif choice == 3:
            print("View Cart\n")
        elif choice == 4:
            print("View History\n")
        elif choice == 5:
            print("Pay for cart\n")
        elif choice == 6:
            print("Browse Bricks\n")
            from brickTable.printBrick import printBrick
            printBrick()



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
                storeModeManager()
            elif res == 0:
                storeMode()
        elif choice == 2:
            print("Online mode selected\n")
            onlineMode()
menu()
quit()