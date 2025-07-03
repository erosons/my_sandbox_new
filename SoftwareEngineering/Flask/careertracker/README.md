Using https://github.com/AdmTal/graphviz_site_generator to generate an interactive SVG websites


Flask web page

SET  environment variable 
FLASK_APP=hello.py
bn   => instant synchronization
This allwous you to run
   => flask run

----------------------------------------------------------------------
****Dynamic routes  handling and user Variables passed from  the UI****
----------------------------------------------------------------------
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
    OR return '<h1>Hello, %s!</h1>' % name
    OR return '<h1>Hello, {0}!</h1>'.format(name)
    OR return <h1>Hello, {name}</h1>


***Passing Variables from the template to the view function***
defining datatypes for var
@app.route('/user')
def user():
    return render_templates('user.html', name=name, age=age)


In the html the Jinja2 template engine is used to render the variables
<h1>Hello, {{ name }}!</h1>

*****Working Logical Jinja Variables**
  @app.route('/')
  def index():
    # Retrieve data from the database
    data_list = YourModel.query.all()

    # Pass the data to the Jinja2 template
    return render_template('index.html', user=data_list)


    {% if user %}
        <h1>Hello, {{ user }}!</h1>
    {% else %}
        <h1>Hello, Stranger!</h1>
    {% endif %}

    OR

    for loop
    <ul>
        {% for comment in comments %}
        <li>{{ comment }}</li>
        {% endfor %}
   
    WHILE loop
    {% set sum = 0 %}
    {% while < 0 %}
        {% set sum = sum + i %}
    {% endwhile %}


Jinja templatings  <!-- Used for dynamically  interacting between the python and the html-->

Template Inherihane  {% extends 'base.html%}  <!-- can be used for inheritance Templating and Management -->

Looping {% for in list %}
         {% endfor %}

Variable=> {{variable}}

For blocking =>
    {% block content %}
    {5 endblock %}

This Class allows us to instantite connection with a database

class SQLAlchemy(
    app: Flask | None = None,
    *,
    metadata: MetaData | None = None,
    session_options: dict[str, Any] | None = None,
    query_class: type[Query] = Query,
    model_class: _FSA_MCT@__init__ = Model,
    engine_options: dict[str, Any] | None = None,
    add_models_to_shell: bool = True,
    disable_autonaming: bool = False
)