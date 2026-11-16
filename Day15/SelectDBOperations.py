import mysql.connector

'''try:
    conn = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="mydb")
    curs = conn.cursor()
    curs.execute("select * from student")
    for row in curs.fetchall():
        print(row)
    conn.close()
except:
    print("Error")'''

#or

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="mydb")
    curs = conn.cursor()
    curs.execute("select * from student")
    for row in curs:
        print(row[0],row[1])
    conn.close()
except:
    print("Error")