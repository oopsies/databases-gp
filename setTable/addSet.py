import mysql.connector, random

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def addSet():
    print("1. Create New Set")
    print("2. Add to existing Set")
    choice=int(input("Option:"))
    
    if choice == 1:
        sql="INSERT INTO  Set_t (set_id,name,brick_id,bricks_needed) VALUES (%s,%s,%s,%s) "
        id = random.randint(00000,99999)
        name=input("What would you like the name of the set to be? \nname:")
        mycursor.execute("SELECT id, name FROM Bricks")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        brick_id="none"
        while brick_id == "none":
            brick_id=input("Insert the id of the desired part you want added to the set:")
            mycursor.execute("SELECT *FROM Bricks WHERE id= "+brick_id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("Not a valid brick number please try again")
                brick_id="none"
        bricks_needed=input("Insert the number of these parts you need for the set:")
        val=(str("%05d"%id),name,brick_id,bricks_needed)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.execute("SELECT *FROM Set_t WHERE set_id="+str("%05d"%id))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print(mycursor.rowcount,"record inserted.\n")

    elif choice == 2:
        sql="INSERT INTO  Set_t (set_id,name,brick_id,bricks_needed) VALUES (%s,%s,%s,%s) "
        mycursor.execute("SELECT *FROM Set_t")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        id="none"
        res="none"
        while id == "none":
            id=input("Insert set_id from one of the existing parts:")
            mycursor.execute("SELECT DISTINCT name FROM Set_t WHERE set_id="+id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("Not a valid brick number please try again")
                id="none"
            else:
                for x in myresult:
                    res=x
        name=res[0]
        mycursor.execute("SELECT id, name FROM Bricks")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        brick_id="none"
        while brick_id == "none":
            brick_id=input("Insert the id of the desired part you want added to the set:")
            mycursor.execute("SELECT *FROM Bricks WHERE id= "+brick_id)
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                print("Not a valid brick number please try again")
                brick_id="none"
        bricks_needed=input("Insert the number of these parts you need for the set:")
        val=(id,name,brick_id,bricks_needed)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.execute("SELECT *FROM Set_t WHERE set_id="+id)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print(mycursor.rowcount,"record inserted.\n")
    else:
        print("Invalid Choice\n\n")
        addSet()
        

