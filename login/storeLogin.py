import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore"
)

mycursor = mydb.cursor()

def storeLogin():
    attempts=0
    accessStatus=0
    for x in range(4):
        user="\'"+input("username:")+"\'"
        password="\'"+input("password:")+"\'"
        sql="SELECT * FROM Employees WHERE id="+user+" AND pin="+password
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        y=len(myresult)
        if y == 0:
            print("Incorrect Password/Username Try Again")
            attempts+=1
        else:
            print("Access Granted")
            for i in myresult:
                print(i)
            accessStatus=1
            break
    if attempts==4:
        print("Too many incorrect guesses")
    return accessStatus
storeLogin()