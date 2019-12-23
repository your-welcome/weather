from flask import Flask, render_template, redirect, flash, url_for

from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '2938hacvw98y213rn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=True, nullable=False)
    zipcode = db.Column(db.String(5), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def display_weather():
    if current_user.is_authenticated:
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=' + current_user.zipcode + ',us&units=imperial&appid=118e5c233596829cee385d6d18f89d46').json()
        weather_data = {
            "city" : r['name'],
            "temp" : r['main']['temp'],
            "humidity" : r['main']['humidity'],
            "description" : r['weather'][0]['description']
        }
        return render_template('weather.html', title='Weather', weather_data = weather_data)
    else:
        return render_template('weather.html', title='Weather')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.user.data, password=form.password.data, zipcode=form.zipcode.data)
        db.session.add(user)
        db.session.commit()
        flash('account created successfully')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user.data).first()
        if user:
            login_user(user)
            return redirect('/')
        else:    
            flash('login failed')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/account', methods=['GET', 'POST'])
def account():
    return 'account'

if __name__ == "__main__":
    app.run(debug=True)