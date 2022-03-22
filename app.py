from flask import Flask
from flask import render_template, request
import mysql.connector
mydb = mysql.connector.connect(
  host="eishwesin.mysql.pythonanywhere-services.com",
  user="eishwesin",
  passwd="thesisproject",
  database="eishwesin$studentdb"
)
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('login.html')
@app.route("/change", methods=['POST'])
def change():
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
           mycursor.execute("SELECT * FROM studentrecordnew WHERE id=1")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 1:",records=records)
       elif studentid == "2":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE id=2")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 2:",records=records)
       elif studentid == "3":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE id=3")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 3:",records=records)
       elif studentid == "4":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE id=4")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 4:",records=records)
       elif studentid == "5":
           mycursor = mydb.cursor()
           mycursor.execute("SELECT * FROM studentrecordnew WHERE id=5")
           records = mycursor.fetchall()
           return render_template('show.html',idnumber="Student id 5:",records=records)
       else:
           return render_template('show.html')

if __name__ == "__main__":
    app.run(host='172.20.10.7', port=8050)