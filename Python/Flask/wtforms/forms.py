from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

class TestForm(FlaskForm):
    username = StringField('Username',validators = [InputRequired()])
    email = StringField('Email',validators = [InputRequired(), Email()])
    favorite_food = StringField('Favorite Food',validators = [InputRequired()])
    submit = SubmitField('Submit')
