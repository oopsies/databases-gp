import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def viewSetSum():
    mycursor.execute("SELECT DISTINCT set_id, name FROM Set_t")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    set_id="none"
    while set_id == "none":
        set_id=input("Insert desired Set_id:")
        mycursor.execute("SELECT *FROM Set_t WHERE set_id="+set_id)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("Invalid ID")
            set_id="none"
        else:
            mycursor.execute("SELECT SUM(bricks_needed*price) FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult=mycursor.fetchall()
            for x in myresult:
                print(set_id+" has a price of $"+str(x[0]))

viewSetSum()