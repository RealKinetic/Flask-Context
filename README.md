Flask-Context
=============

Supply an arbitrary context object to Flask and use it in your application.

After many years of writing apps, we (Real Kinetic) decided that one of the
most pragmatic things you can do for the long term stabilty and maintainability
of your app is to use and pass round a context object that has access to all
the business level state that you need. This should be passed around everywhere
so when debugging you can figure out what request the problem occurred in.

One of the simplest examples is that of a correlation id. Let's imagine a
microservice environment with a single request that comes in from the outside
is potentially handled by one or more services. When you start distributing
requests like that it becomes really hard to debug errors when they occur. It
would be extremely useful if a unique token was used to tie all of the
processing done by the various services together so that any logging aggregation
could make it easy to get a better picture of what happened. This is where
projects like openzipkin come in.

Other examples may include passing round a ``user_id`` for the request.

This library extracts the Flask specifics so the engineer can focus on the
business problem.

Usage
-----

```python
import uuid
from flask import Flask
from flask_context import FlaskContext, current_context


class MyContext(object):
    def __init__(self, correlation_id=None):
        self.correlation_id = correlation_id or uuid.uuid4().hex


app = Flask(__name__)

flask_ctx = FlaskContext(MyContext, app)


@app.route('/')
def index():
    return current_context.correlation_id


if __name__ == '__main__':
   app.run('127.0.0.1', 5000)
```

Head on over to ``http://127.0.0.1:5000/'`` and you should see a unique id
everytime you refresh the page.

Development
-----------

Setting up:

```bash
$ mkvirtualenv flask-context
(flask-context) $ pip install -r requirements_dev.txt
```

Running the tests:

```bash
(flask-context) $ nosetests --with-coverage
```
