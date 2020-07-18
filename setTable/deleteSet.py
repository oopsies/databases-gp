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

    elif choice == 2:
        mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        id="none"
        while id == "none":
            id=input("Insert set_id you want to delete bricks from:")
            mycursor.execute("SELECT *FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE Set_t.set_id="+id)
            myresult = mycursor.fetchall()
            if len(myresult)==0:
                print("Invalid ID")
                id="none"
            else:
                for x in myresult:
                    print(x) 
        brick_id="none"
        while brick_id == "none":
            brick_id=input("Which brick do you want deleted from the set?\nbrick_id:")
            mycursor.execute("SELECT *FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE Set_t.set_id="+id+" AND Bricks.id="+brick_id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("Brick is not apart of set")
                brick_id="none"
            else:
                mycursor.execute("DELETE FROM Set_t WHERE set_id="+id+" AND brick_id="+brick_id)
                mydb.commit()
                for x in myresult:
                    print(x)
    else:
        print("Invalid Choice")
        deleteSet()
deleteSet()