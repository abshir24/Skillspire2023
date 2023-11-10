from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route('/process-data', methods = ['GET', 'POST'])

def processData():
    return render_template("data.html", userdata = request.form)

# user inputs data => data moves to request.form object on server => data gets sent back to user


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
