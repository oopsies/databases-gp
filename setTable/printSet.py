import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def printSet():
    print("1. Print All Sets")
    print("2. Print Specific Set and its Bricks")
    print("3. Print Sets based on attributes")
    print("4. Back")
    choice=int(input("Option:"))

    if choice == 1:
        mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print("Check individual Brick for more information")
    elif choice == 2:
        set_id="none"
        while set_id == "none":
            set_id=input("Insert set_ID:")
            mycursor.execute("SELECT *FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE Set_t.set_id="+set_id)
            myresult=mycursor.fetchall()
            if len(myresult) == 0:
                print("Invalid ID")
                #set_id="none"
            else:
                for x in myresult:
                      print(x)
                mycursor.execute("SELECT SUM(bricks_needed*price) FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
                myresult=mycursor.fetchall()
                for x in myresult:
                    print(set_id+" has a price of $"+str(x[0]))
            
    elif choice == 3:
        sql="SELECT * FROM Set_t WHERE "
        attr = input("What is the attribute you are searching for(ex. set_id, name, brick_id, bricks_needed )?")
        print("Example input values set_id=12345,name=Playhouse,brick_id=11123,bricks_needed=6")
        val ="\'"+input(attr+"=")+"\'"
        record = attr+"="+val
        sql=sql+record
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    elif choice == 4:
        return
    else:
        print("Invalid Option")