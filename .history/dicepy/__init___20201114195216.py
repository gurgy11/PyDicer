import os

from flask import Flask, render_template
from dotenv import load_dotenv
from flask.globals import current_app

# Local imports
from .settings import *
import dicepy.lib.middleware.auth_middleware as auth_middleware

# Load environment variables
load_dotenv()

def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    print(auth_middleware.login_required())

    @app.route('/')
    @app.route('/index')
    @auth_middleware.login_required
    def index():
        return render_template('index.html', title='DicePy - Index')

    ''' Blueprint Imports and Registration '''

    from dicepy.modules.addresses import addresses_bp
    app.register_blueprint(addresses_bp)
    app.add_url_rule('/', endpoint='addresses')

    from dicepy.modules.auth import auth_bp
    app.register_blueprint(auth_bp)
    app.add_url_rule('/', endpoint='auth')

    return app
