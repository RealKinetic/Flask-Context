import unittest

from flask import Flask

from flask_context import current_context
from flask_context import FlaskContext


class ContextTestCase(unittest.TestCase):
    def test_extension(self):
        """
        Ensure that the application's extension is set up correctly.
        """
        app = Flask(__name__)

        ext = FlaskContext(None, app)

        self.assertIs(ext.app, app)
        self.assertIs(ext, app.extensions['flask_ctx'])

    def test_init_app(self):
        """
        Flask allows for delayed instantiation. Let's support that.
        """
        app = Flask(__name__)

        ext = FlaskContext(None)

        # some time passes ..
        ext.init_app(app)

        self.assertIs(ext.app, app)
        self.assertIs(ext, app.extensions['flask_ctx'])

    def test_request(self):
        """
        Ensure that getting the context while in a request works as expected.
        """
        # sentinel
        sentinel = object()
        app = Flask(__name__)

        ext = FlaskContext(lambda: sentinel, app)

        @app.route('/')
        def index():
            self.assertIs(ext.get_current_context(), sentinel)

            return ''

        with app.test_client() as client:
            client.get('/')


class CurrentContextTestCase(unittest.TestCase):
    def test_current_context(self):
        """
        Check the `current_context` helper to ensure basic sanity checks pan
        out.
        """
        class TestContext(object):
            correlation_id = 'unit-test'

        app = Flask(__name__)

        FlaskContext(TestContext, app)

        @app.route('/')
        def index():
            self.assertEqual(current_context.correlation_id, 'unit-test')

            return ''

        with app.test_client() as client:
            client.get('/')
