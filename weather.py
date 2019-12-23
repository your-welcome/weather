from flask import Flask, render_template, redirect, flash, url_for
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2938hacvw98y213rn'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('account created successfully')
        return redirect('/register')
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Login', form=form)

@app.route('/account', methods=['GET', 'POST'])
def account():
    return 'account'

if __name__ == "__main__":
    app.run(debug=True)