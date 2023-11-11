from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route("/",  methods = ['GET', 'POST']) 
def index():
    if request.method == "POST":
        session['username'] = request.form["username"]
        session['email'] = request.form["email"]
        session['favorite_food'] = request.form['favorite_food']
        return render_template("index.html")        
    
    return render_template("index.html")

@app.route('/process-data', methods = ['GET', 'POST'])

def processData():
    return render_template("data.html", userdata = request.form)



if __name__ == "__main__":
    app.run(debug = True, port = 5000)
