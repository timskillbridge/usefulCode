
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# students = [
#     {'id':'1', 'first_name':'John','last_name':'Williams','age':'18','grade':'A'},
#     {'id':'2', 'first_name':'Justin','last_name':'Margera','age':'12','grade':'C'},
#     {'id':'3', 'first_name':'Mary','last_name':'Rogers','age':'21','grade':'B'},
#     {'id':'4', 'first_name':'Steve','last_name':'Mickinley','age':'14','grade':'C'},
#     {'id':'5', 'first_name':'Phil','last_name':'Dasta','age':'25','grade':'A'},
#     ]

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg://wtadam2:]@localhost/school'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birthdate = db.Column(db.Integer)
    address_id = db.Column(db.String(1))


# methods = takes a list with items in single quotes and capitalized.
@app.route('/students', methods = ['GET'])
def get_students():
    # Select all students
    studs_from_db = Students.query.all()
    students = []
    for stud in studs_from_db:
        students.append(
            {
                "id": stud.id,
                "first_name": stud.first_name,
                "last_name": stud.last_name,
                "birthday": stud.birthdate,
                "address_id": stud.address_id,
            }
        )
    
    # SELECT * FROM students;
    print(Students.query.all())
    return jsonify(students)

# Triggered at page load
# all routes will be prefaced by http://127.0.0.1:8000 or whatever port you specify in app.run()
@app.route("/",methods=['GET'])
def home():
    return "<h1>Hello from the server</h1>"



# Port is optional
app.run(debug=True, port=8000)


app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)