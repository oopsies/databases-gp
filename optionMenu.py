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

def report():
    def invReport():
        type = 0
        while type != 4:
            print("What inventory would you like to see?")
            print("1. Inventory under a certain quantity")
            print("2. Inventory over a certain quantity")
            print("3. All inventory")
            print("4. Back")
            type = int(input("Option:"))
            if type == 1:
                thresh = int(input("Choose quantity threshold: "))
                mycursor.execute("SELECT * FROM Bricks WHERE quantity < %d" % (thresh))
                print("('BrickID', 'BrickName', 'Quantity', 'Price')")
                for x in mycursor.fetchall():
                    print(x)
            elif type == 2:
                thresh = int(input("Choose quantity threshold: "))
                mycursor.execute("SELECT * FROM Bricks WHERE quantity > %d" % (thresh))
                print("('BrickID', 'BrickName', 'Quantity', 'Price')")
                for x in mycursor.fetchall():
                    print(x)
            elif type == 3:
                mycursor.execute("SELECT * FROM Bricks")
                print("('BrickID', 'BrickName', 'Quantity', 'Price')")
                for x in mycursor.fetchall():
                    print(x)

    def saleReport():
        period = 0
        while period != 3:
            print("What time period would you like to view?")
            print("1. Monthly sales")
            print("2. Weekly sales")
            print("3. Daily sales")
            print("4. Back")
            period = int(input("Option:"))
            if period == 1:
                store = input("Choose store: ")
                print(store)
                mycursor.execute("SELECT * FROM Employees WHERE store_preference = '%s'" % (store))
                print("('ID', 'Name', 'Store', 'Pin')")
                for x in mycursor.fetchall():
                    print(x)
            elif period == 2:
                mycursor.execute("SELECT * FROM Employees")
                print("('ID', 'Name', 'Store', 'Pin')")
                for x in mycursor.fetchall():
                    print(x)

    def employeeReport():
        type = 0
        while type != 3:
            print("What employees would you like to see?")
            print("1. Employees from a certain store")
            print("2. All employees")
            print("3. Back")
            type = int(input("Option:"))
            if type == 1:
                store = input("Choose store: ")
                print(store)
                mycursor.execute("SELECT * FROM Employees WHERE store_preference = '%s'" % (store))
                print("('ID', 'Name', 'Store', 'Pin')")
                for x in mycursor.fetchall():
                    print(x)
            elif type == 2:
                mycursor.execute("SELECT * FROM Employees")
                print("('ID', 'Name', 'Store', 'Pin')")
                for x in mycursor.fetchall():
                    print(x)

    def poopy():
        return 5

    choice = 0
    while choice != 4:
        print("Choose report type:")
        print("1. Inventory Report")
        print("2. Sales Report")
        print("3. Employee Report")
        print("4. Back")
        choice = int(input("Option:"))
        if choice == 1:
            invReport()
        elif choice == 2:
            x = 5
        elif choice == 3:
            employeeReport()






def storeMode():
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
        elif choice == 3:
            print ("Reports\n")
            report()
        elif choice == 4:
            print ("Item Management\n")
            item()
        elif choice == 5:
            print ("Payment\n")
        elif choice == 6:
            print("Sale\n")
            cart()

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
                storeMode()
        elif choice == 2:
            print("Online mode selected\n")
            onlineMode()
menu()