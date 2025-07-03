from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)

# Define your database model
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    your_column = db.Column(db.String(255),nullable=False, unique=True)
    your_column2 = db.Column(db.String(length=255),nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    # Retrieve data from the database
    data_list = YourModel.query.all()

    # Pass the data to the Jinja2 template
    return render_template('index.html', data_list=data_list)

if __name__ == '__main__':
    app.run(debug=True)
