import mysql.connector, random

mydb = mysql.connector.connect(
        host="localhost",
        user="tester",
        password="tester",
        database="LegoStore"
)

mycursor = mydb.cursor()

def testInserts():
    sql="INSERT INTO Set_t(set_id, name, brick_id, bricks_needed) VALUES (%s,%s,%s,%s) "
    id = random.randint(00000,99999)
    entry=(str("%05d"%id),"Full Lego Body","58126","1")
    entry2=(str("%05d"%id),"Full Lego Body","69413","1")
    entry3=(str("%05d"%id),"Full Lego Body","76304","2")
    entry4=(str("%05d"%id),"Full Lego Body","83940","2")
    mycursor.execute(sql,entry)
    mycursor.execute(sql,entry2)
    mycursor.execute(sql,entry3)
    mycursor.execute(sql,entry4)
    mydb.commit()
    mycursor.execute("SELECT DISTINCT name FROM Set_t")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
testInserts()