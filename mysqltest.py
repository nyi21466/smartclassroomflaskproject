import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="eishwesin.mysql.pythonanywhere-services.com",
  user="eishwesin",
  passwd="thesisproject",
  database="eishwesin$studentdb"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE studentrecordnew (id INT(11), name VARCHAR(50))")
mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('2',datetime.datetime.now()))
mydb.commit()
print(mycursor.rowcount, "record inserted.")

