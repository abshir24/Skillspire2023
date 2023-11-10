from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def homePage():
    phone_book = { 
        "Abshir": 5555555,
        "Elon": 8890531
    }
    return render_template("index.html", numbers = [1,2,3,4,5])

@app.route("/about")
def aboutPage():     
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug = True, port = 5000)
