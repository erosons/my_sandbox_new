from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def Home_page():
    return render_template('index.html')

@app.route("/about")
def About_page():
    return '<h1> Hello About Page </h1>'

#Dynamic routes handling
@app.route('/about/<name>')
def user(name):
    return '<h1>Hello About Page {}!</h1>'.format(name)



