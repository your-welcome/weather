from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class RegisterForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=15)])
    zipcode = IntegerField('Zip Code', validators=[DataRequired(), NumberRange(min=10000, max=99999, message = "Must be exactly 5 Digits.")])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')