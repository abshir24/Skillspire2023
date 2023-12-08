from flask import Flask, render_template, request,redirect,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test3.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref = 'user')
    created_on = db.Column(db.DateTime, server_default=db.func.now())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable = False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register', methods = ["GET","POST"])
def register():
    user = User.query.filter_by(email = request.form['email']).first()

    if user == None:
        newUser = User(username = request.form['username'], email = request.form['email'], password = request.form['email'])
        db.session.add(newUser)
        db.session.commit()
        
        user = User.query.filter_by(email = request.form['email']).first()
        session['user_id'] = user.id
        return render_template('wall.html')
    else:
        return redirect('/wall')

@app.route('/login', methods = ["GET","POST"])
def login():
    user = User.query.filter_by(email = request.form['email']).first()

    if user != None:
        session['user_id'] = user.id
        
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/wall', methods = ["GET","POST"])
def wall():
   user = User.query.get(session['user_id'])
   all_posts = Post.query.all()
    
   return render_template('wall.html', user = user, all_posts = all_posts)

@app.route('/addpost', methods = ["GET","POST"])
def post():
   post = Post(post = request.form['post'], user_id = session['user_id'])

   db.session.add(post)
   db.session.commit()

   return redirect('/wall')

if __name__ == "__main__":
     with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)