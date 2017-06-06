"""
Flask-Context allows the user to provide an arbitrary context object that will
be created at the beginning of the request/when first accessed.

This is useful for passing things round like a correlation_id/user_id that is
application specific.

Very useful for microservice type environments.

Usage::

    import uuid
    from flask import Flask
    from flask_context import FlaskContext, current_context


    class MyContext(object):
        def __init__(self, correlation_id=None):
            self.correlation_id = correlation_id or uuid.uuid4().hex()

    app = Flask(__name__)

    flask_ctx = FlaskContext(MyContext, app)

    @app.route('/')
    def index():
        return current_context.correlation_id
"""

from flask_context.context import FlaskContext, current_context, get_ext

__all__ = [
    'FlaskContext',
    'current_context',
    'get_ext',
]
