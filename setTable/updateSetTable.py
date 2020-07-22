import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def updateSet():
    print("1. Update Particular Set")
    print("2. Update Brick information in a particular set")
    choice=int(input("Option:"))
    
    if choice == 1:
        mycursor.execute("SELECT *FROM Set_t INNER JOIN BRICKS ON Set_t.brick_id=Bricks.id")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        set_id="none"
        while set_id == "none":
            set_id=input("Insert set_ID:")
            mycursor.execute("SELECT *FROM Set_t INNER JOIN BRICKS ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult=mycursor.fetchall()
            if len(myresult) == 0:
                print("Invalid ID")
                set_id="none"
            else:
                for x in myresult:
                    print(x)
                sql = "UPDATE Set_t SET  "
                attr=input("What attribute would you like to change(set_id,name,brick_id,bricks_needed)?\nSuggestion:Only change set_id or name using this option\n Option:")
                val ="\'"+input(attr+"=")+"\'"
                record = attr+"="+val
                sql = sql+record+" WHERE set_id="+set_id
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute("SELECT *FROM Set_t WHERE "+attr+"="+val)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print(mycursor.rowcount,"record(s) affected\n")
    elif choice == 2:
        mycursor.execute("SELECT *FROM Set_t INNER JOIN BRICKS ON Set_t.brick_id=Bricks.id")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        set_id="none"
        while set_id == "none":
            set_id=input("Insert set_ID:")
            mycursor.execute("SELECT *FROM Set_t INNER JOIN BRICKS ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult=mycursor.fetchall()
            if len(myresult) == 0:
                print("Invalid ID")
                set_id="none"
            else:
                for x in myresult:
                     print(x)
                brick_id="none"
                while brick_id=="none":
                    brick_id=input("Insert brick_ID:")
                    mycursor.execute("SELECT *FROM Set_t INNER JOIN BRICKS ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id+" AND Bricks.id="+brick_id)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        print("Invalid ID")
                        brick_id="none"
                    else:
                        sql = "UPDATE Set_t SET  "
                        attr = input("What value would you like to change(set_id, name, brick_id, bricks_needed)?")
                        print("Example of input values set_id=12345, name=PLayhouse, brick_id=1123, bricks_needed=4")
                        val = "\'"+input(attr+"=")+"\'"
                        record = attr+"="+val
                        sql = sql+record+" WHERE set_id="+set_id+" AND brick_id="+brick_id
                        mycursor.execute(sql)
                        mydb.commit()
                        print(mycursor.rowcount,"record(s) affected\n")
