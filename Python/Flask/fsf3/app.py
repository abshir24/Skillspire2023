from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())


@app.route('/')
def index():
    # [<Course1>, <Course2>]
    return render_template("index.html", courses = Course.query.all())

@app.route('/addcourse', methods=["POST", "GET"])
def addCourse():
    course = Course(name=request.form['coursename'], 
                    description=request.form['description'])
    db.session.add(course)
    db.session.commit()

    return redirect('/')

@app.route('/removecourse/<int:courseid>')
def removeCourse(courseid):
    return render_template("delete.html", course = Course.query.get(courseid))
    
@app.route('/delete/<int:courseid>')
def delete(courseid):
    course =  Course.query.get(courseid)
    db.session.delete(course)
    db.session.commit() 

    return redirect('/')

if __name__ == "__main__":
     with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)