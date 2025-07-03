Flask web page

SET  environment variable 
FLASK_APP=hello.py
FLASK_DEBUG=1   => instant synchronization
This allwous you to run
   => flask run

Dynamic routes handling
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
    OR return '<h1>Hello, %s!</h1>' % name
    OR return '<h1>Hello, {0}!</h1>'.format(name)
    OR return <h1>Hello, {name}</h1>