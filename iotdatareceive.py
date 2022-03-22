import mysql.connector
mydb = mysql.connector.connect(
  host="eishwesin.mysql.pythonanywhere-services.com",
  user="eishwesin",
  passwd="thesisproject",
  database="eishwesin$studentdb"
)

import thingspeak
import datetime
import time
hours = 6
channel_id = 1108445 # PUT CHANNEL ID HERE
read_key = 'I8WLAGN069X181XN'  # PUT YOUR WRITE KEY HERE
channel = thingspeak.Channel(id=channel_id, api_key=read_key)
a = channel.get_field_last(field="field1")
oldentry = a[48:51]
while 1:
    a = channel.get_field_last(field="field1")
    #print(a)
    entry = a[48:51]
    if entry != oldentry:
        if a[49:50] == ',':
            result = a[60:61]
            print(result)
            if result == "1":
                print("id1")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('1',datetime.datetime.now()))
                #print(datetime.timedelta(hours=hours))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "2":
                print("id2")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('2',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "3":
                print("id3")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('3',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "4":
                print("id4")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('4',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "5":
                print("id5")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('5',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
        elif a[50:51] == ',':
            result = a[61:62]
            print(result)
            if result == "1":
                print("id1")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('1',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "2":
                print("id2")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('2',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "3":
                print("id3")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('3',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "4":
                print("id4")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('4',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "5":
                print("id5")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('5',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
        elif a[51:52] == ',':
            result = a[62:63]
            print(result)
            if result == "1":
                print("id1")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('1',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "2":
                print("id2")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('2',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "3":
                print("id3")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('3',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "4":
                print("id4")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('4',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
            elif result == "5":
                print("id5")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO studentrecordnew(id,name) VALUES(%s, %s)", ('5',datetime.datetime.now()))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                time.sleep(15)
        oldentry = entry




