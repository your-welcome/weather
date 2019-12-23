from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class RegisterForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=15)])
    zipcode = StringField('Zip Code', validators=[DataRequired(), Length(min=5, max=5)])
    submit = SubmitField('Register')

    #def validate_user(self, user):
    #    user_count = User.query.filter_by(username=user.data).count()
    #    if user_count > 0:
    #        raise ValidationError('User already exists')

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')