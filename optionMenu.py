
def employee():
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Print Employee(s)")
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
    print("1. Employee Management")
    print("2. Order Management")
    print("3. Reports")
    print("4. Search Item")
    print ("5. Payment")
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
    print("1. Store Mode")
    print("2. Online Mode")
    choice=int(input("Option:"))
    if choice == 1:
        print("Store mode selected\n")
        storeMode()
    if choice == 2:
        print("Online mode selected\n")
menu()