from flask import current_app
from flask import request

from werkzeug.local import LocalProxy


__all__ = [
    'current_context',
    'FlaskContext',
    'EXTENSION_NAME',
]

EXTENSION_NAME = 'flask_ctx'

current_context = LocalProxy(lambda: get_current_context())


class FlaskContext(object):
    """
    A Flask extension that allows creating and manipulation of a context.

    The context_class is supplied by the user and is instantiated at first
    access. The context resides on the request object and is linked to it's
    lifecycle.
    """

    ctx_attr_name = '_flask_ctx'

    def __init__(self, context_class, app=None):
        self.context_class = context_class
        self.app = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.extensions[EXTENSION_NAME] = self

    def make_context(self, *args, **kwargs):
        return self.context_class(*args, **kwargs)

    def get_current_context(self):
        ctx = getattr(request, self.ctx_attr_name, None)

        if ctx:
            return ctx

        ctx = self.make_context()

        self.set_context(ctx)

        return ctx

    def set_context(self, context):
        setattr(request, self.ctx_attr_name, context)


def get_ext(app=None):
    """
    A helper method to get the :ref:`FlaskContext` instance attached to the
    :ref:`Flask` application.

    If the extension could not be found, an :ref:`EnvironmentError` is raised.

    :param app: The :param:`Flask` app. If not supplied, the `current_app` will
        be used.
    """
    app = app or current_app

    try:
        return app.extensions[EXTENSION_NAME]
    except KeyError:
        raise EnvironmentError('Failed to get the FlaskContext extension')


def get_current_context():
    """
    Returns the current context of the Flask request
    """
    ext = get_ext()

    return ext.get_current_context()
