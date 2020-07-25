import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()
name=""

def deletePayment(user):
    if user == "":
        user="Guest"
    mycursor.execute("SELECT *FROM Payment WHERE user=\'"+user+"\'")
    myresult = mycursor.fetchall()
    mycursor.execute("DELETE FROM Payment WHERE user=\'"+user+"\'")
    mydb.commit()
    for x in myresult:
        print(x)