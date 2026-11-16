import mysql.connector


#insert, update, delete
'''conn = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="mydb")
curs = conn.cursor()
curs.execute("INSERT INTO student VALUES(107,'XYZ');")
conn.commit()
conn.close()'''

#or

#insert_query="INSERT INTO student VALUES(107,'XYZ');"
#update_query="UPDATE student SET sname='Priyanka' WHERE sid = '102';"
delete_query="DELETE FROM student WHERE sid = '107';"

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="mydb")
    curs = conn.cursor()
    #curs.execute(insert_query)
    #curs.execute(update_query)
    curs.execute(delete_query)
    conn.commit()
    conn.close()
except:
    print("Connection Unsuccessful")





