import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def updateEmployee():
    sql = "UPDATE employees SET "
    newAttr = input("What value would you like to change(id,name,store_preference)?")
    newVal = "\'"+input("What value do you want?\n"+newAttr+"=")+"\'"
    targetAttr = input("Which attributes are you searching for(id,name,store_preference)?")
    targetVal = "\'"+input("What value does it have?\n"+targetAttr+"=")+"\'"
    sql = sql + newAttr +"="+newVal+" WHERE "+targetAttr+"="+targetVal
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"record(s) affected")
updateEmployee()