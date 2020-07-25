import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="tester",
    database="LegoStore",
    autocommit=True
)

mycursor = mydb.cursor()

def createSetTable():
    sql = "CREATE TABLE Set_t (set_id VARCHAR(5) NOT NULL,"\
          "name VARCHAR(255) NOT NULL,"\
          "brick_id VARCHAR(5) NOT NULL,"\
          "bricks_needed INT NOT NULL,"\
          "PRIMARY KEY (set_id,brick_id))"
    mycursor.execute(sql)
createSetTable()
mycursor.execute("DESCRIBE Set_t")
for x in mycursor:
    print(x)
