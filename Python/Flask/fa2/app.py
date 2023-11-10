from flask import Flask, render_template

app = Flask(__name__) 

# @app.route('/<route_param>/<value>')

# def index(route_param,value): 
#     img= ""
#     if("vacation" in route_param):
#         img="vacation"
#     if("food" in route_param):
#         img = "food"

#     return render_template("index.html", value = value, imagetest = img)

@app.route('/')

def index(): 

    return render_template("index.html")

@app.route('/display-name')

def displayName():
    return render_template("name.html")

@app.route('/display-food')

def displayFood():
    return render_template("food.html")

@app.route('/display-vacation')

def displayVacation():
    return render_template("vacation.html")

if __name__  == '__main__':
   app.run(debug = True, port = 5000) 