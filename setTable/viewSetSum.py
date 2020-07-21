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
            i = 0
            mult=[0]*len(myresult)
            prices=[0]*len(myresult)
            newprices=0
            mycursor.execute("SELECT Bricks.price FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult = mycursor.fetchall()
            for x in myresult:
                prices[i]=x[0]
                i=i+1
            mycursor.execute("SELECT bricks_needed FROM Set_t RIGHT JOIN Bricks ON Set_t.brick_id=Bricks.id WHERE set_id="+set_id)
            myresult = mycursor.fetchall()
            i=0
            for x in myresult:
                mult[i]=x[0]
                i=i+1
            i=0
            for x in range(0,4):
                newprices=newprices+(mult[i]*prices[i])
                i=i+1
            print(set_id+"  has a set price of "+str(newprices))


viewSetSum()