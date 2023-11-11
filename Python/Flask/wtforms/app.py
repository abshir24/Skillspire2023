from flask import Flask, render_template, request
from forms import TestForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

@app.route("/", methods =["POST","GET"]) 
def index():
    form = TestForm()

    if form.validate_on_submit(): # If the form is valid (No empty inputs, No validation errors)
        # Data handling portion if form data is valid
        user_data = {
            "username":form.username.data, # request.form["username"]
            "email": form.email.data, # request.form["email"]
            "favorite_food": form.favorite_food.data # request.form["favorite_food"]
        }
        return render_template("index.html",form=form, user_data = user_data)
       
        

    return render_template("index.html",form = form)



if __name__ == "__main__":
    app.run(debug = True, port = 5000)