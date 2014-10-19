from flask import Flask, request, g, render_template
from Complain import Complaint_List
import sqlite3

complaints = Complaint_List()
app = Flask(__name__)
#DATABASE = 'complaints.db'

#def get_db():
#    db = getattr(g, '_database', None)
#    if db is None:
#        db = g._database = sqlite3.connect(DATABASE)
#    return db


#def db_read():
#    cur = get_db().cursor()
#    cur.execute("SELECT * FROM complaints")
#    return cur.fetchall()

#def db_add(complaint):
#    cur = get_db().cursor()
#    cur.execute("INSERT INTO complaints VALUES (?)", complaint)
#    get_db().commit()

@app.route("/")
def home():
    all_complaints = complaints.get_complaints()
    return render_template('index.html', all_complaints = all_complaints)

@app.route("/complain", methods=["POST"])
def receive_complaint():
    complaints.add_complaint(request.form['complaint'])
    return home()
    

@app.route("/salt/<complaint_id>")
def salt(complaint_id):
    complaint_id = int(float(complaint_id))
    complaints.salt(complaint_id)
    return home()

@app.route("/pepper/<complaint_id>")
def pepper(complaint_id):
    complaint_id = int(float(complaint_id))
    complaints.pepper(complaint_id)
    return home()


if __name__ == "__main__":
    app.debug = True
    app.run()
