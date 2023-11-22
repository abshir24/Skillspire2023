from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/userdata', methods=["GET","POST"])
def userData(): 
    if request.method == "POST":
        new_user = User(email = request.form["email"], password = request.form["password"])    
        db.session.add(new_user)
        db.session.commit()

    # Retrieval
    users = User.query.all() #[<User1>,<User2>,<User3>]

    return render_template("users.html", users = users)

@app.route('/login', methods=["GET","POST"])
def login():
    user = User.query.filter_by(email=request.form['email']).first()
    if user == None or user.password != request.form['password']: 
        return render_template("index.html")
    else:
        return render_template("user.html",email=user.email)
    

@app.route('/updateuser/<email>')
def update(email):
    user = User.query.get(email)

    user.email = "email@email.com"
    user.password = "12345"

    db.session.commit()

    return render_template("user.html",email=user.email)

@app.route('/deleteuser/<email>')
def delete(email):
    user = User.query.get(email)

    db.session.delete(user)

    db.session.commit()

    return redirect('/userdata')

    


if __name__ == "__main__":
     with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)