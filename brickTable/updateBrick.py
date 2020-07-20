import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "tester",
    password = "tester",
    database = "LegoStore"
)

mycursor = mydb.cursor()

def updateBrick():
    sql = "UPDATE Bricks SET "
    newAttr = input("What value would you like to change(id,name,quantity,price)?")
    newVal = "\'"+input("What value do you want?\n"+newAttr+"=")+"\'"
    targetAttr = input("What attributes are you searching for(id,name,quantity,price)?")
    targetVal = "\'"+ input("What value does it have?\n"+targetAttr+"=")+"\'"
    sql = sql + newAttr +"="+newVal+" WHERE "+targetAttr+"="+targetVal
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT *FROM Bricks WHERE "+ newAttr+"="+ newVal)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print(mycursor.rowcount,"record(s) affected\n")
updateBrick()