from flask import Flask, render_template

app = Flask(__name__) 


@app.route('/')

def index():
    return "Name:{}, Favorite Food:{}, Vacation:{}".format("Abshir", "Spinach","Santo Domingo")


if __name__  == '__main__':
   app.run(debug = True, port = 5000) 