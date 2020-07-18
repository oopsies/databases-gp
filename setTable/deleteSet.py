import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def deleteSet():
    print("1. Delete whole Set")
    print("2. Delete Brick from Set")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        id=input("Insert set_id you want deleted:")
        mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t WHERE set_id="+id)
        myresult = mycursor.fetchall()
        mycursor.execute("DELETE FROM Set_t WHERE set_id="+id)
        mydb.commit()
        for x in myresult:
            print(x)
        print(mycursor.rowcount,"record(s) deleted\n")

    if choice == 2:
        mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        id=input("Insert set_id you want to delete bricks from:")
        
deleteSet()