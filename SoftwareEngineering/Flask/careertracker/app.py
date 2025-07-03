
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.urandom(24)).replace('b','')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/postgres'  # Replace with your database URL

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/')
@app.route("/home")
def Home_page():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        print(user)
        if user and user.password == password:
            print(user.password)
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('profile_page'))
        else:
           flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')


@app.route("/profilePage")
def profile_page():
    careerList = ['Software Engineer','Technical Product Owner','Data Engineer','Cyber Security']
    return render_template('profile_page.html',CareerList=careerList)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run()