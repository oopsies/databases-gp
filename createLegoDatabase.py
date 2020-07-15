import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE LegoStore")