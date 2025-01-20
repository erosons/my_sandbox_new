docker run --name careerPath -e POSTGRES_PASSWORD=password -e POSTGRES_USER=careerpath -p 5432:5432 -d postgres

Jinja templatings  <!-- Used for dynamically  interacting between the python and the html-->

Template Inherihane  {% extends base.html%}  <!-- can be used for inheritance Templating and Management -->

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

Manually Push a Context on the CLI
    from app import db
    from flask import Flask
    app = Flask(__name__)
    app.app_context()
    db.create_all()

*****Model Changing and Querying the DATABASES****
https://flask-migrate.readthedocs.io/en/latest/
>>pip install Flask-Migrate ==4.0.5

see docs
- flask db init
- $ flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
- $ flask db migrate     # To detect automatically all the changes.
- $ flask db upgrade     # To apply all the changes.

Adding item
============
    from app import Item (the database model)
>>> item3=Item(name="Samsungg",price=600,barcode="19101888",description='desc')
>>> db.session.add(item1)
>>> db.session.commit()
>>> Incase of Error
     - db.session.rollback()

Query your items 
================
 Item.query.all() => returns a list of dictionaries

Iterating over item and printing valuues in a row
===================================================
 [Item Andriod, Item Iphone]
>>> for item in Item.query.all():
...    item.price
...    item.name
...    item.barcode
... 
600
'Andriod'
'19101012'
600
'Iphone'
'19101014'

Filter a query by some specific have and return by iterating
==============================================================
>>> for item in Item.query.filter_by(price = 600):
...  item
>>> for item in Item.query.filter_by(price = 600):
...  item
... 
Item Andriod
Item Iphone
Item Samsungg


==============================================================
Integrating React Flow, which is a React library, with Flask,
===============================================================

brew install node  => Install Node.js

Integrating React Flow, which is a React library, with Flask, a Python web framework, can be done by setting up a front-end and back-end application separately and making them communicate through API endpoints. Here are the general steps to integrate React Flow with Flask:

=============================
Set Up React Flow Front-End:
============================

Create a new React project if you don't have one already. You can use tools like Create React App to quickly generate a project structure.

>>> npx create-react-app my-react-flow-app
>>> cd my-react-flow-app


Install the React Flow library and other dependencies:

>>> npm install react-flow-renderer axios


