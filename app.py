from flask import Flask
from flask import render_template, request
import sqlite3
import random
import datetime

mydb = sqlite3.connect('Makersdatabase.db', check_same_thread=False)
mycursor = mydb.cursor()

mycursor.execute('''
    CREATE TABLE IF NOT EXISTS studentrecordnew (
        Id INT,
        time TIMESTAMP
    )
''')

idlist = [1,2,3,4,5]

# for i in range(30):
#     currentDateTime = datetime.datetime.now()
#     mycursor.execute("INSERT INTO studentrecordnew (Id, time) VALUES (?, ?)", (int(random.choice(idlist)), currentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
#mydb.commit()

app = Flask(__name__)
@app.route("/")
def index():
    # get the current datetime and store it in a variable
    currentDateTime = datetime.datetime.now()
    mycursor.execute("INSERT INTO studentrecordnew (Id, time) VALUES (?, ?)", (int(random.choice(idlist)), currentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
    mydb.commit()
    return render_template('login.html')
@app.route("/change", methods=['POST'])
def change():
    # get the current datetime and store it in a variable
    currentDateTime = datetime.datetime.now()
    mycursor.execute("INSERT INTO studentrecordnew (Id, time) VALUES (?, ?)", (int(random.choice(idlist)), currentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
    mydb.commit()
    if request.method == 'POST':
       name = request.form['name']
       pw = request.form['pw']
       print(name + pw)
       if name == "admin" and pw == "12345":
           return render_template('show.html')
       else:
           return render_template('login.html')

@app.route("/showrecord", methods=['POST'])
def showrecord():
     if request.method == 'POST':
       studentid = request.form['studentid']
       print(studentid)
       if studentid == "1":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE Id=1")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 1:",records=records)
       elif studentid == "2":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE Id=2")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 2:",records=records)
       elif studentid == "3":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE Id=3")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 3:",records=records)
       elif studentid == "4":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE Id=4")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 4:",records=records)
       elif studentid == "5":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE Id=5")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 5:",records=records)
       else:
           return render_template('show.html')

if __name__ == "__main__":
    #app.run(host='172.20.10.4', port=8050)
    app.run(host="0.0.0.0", port=5001, debug=True)
