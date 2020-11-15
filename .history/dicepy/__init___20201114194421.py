import os

from flask import Flask, render_template
from dotenv import load_dotenv

# Local imports
from .settings import *
import dicepy.modules.auth.auth_controller as auth_controller

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

    @app.route('/')
    @app.route('/index')
    @a_controller.login_required
    def index():
        a_controller = auth_controller.AuthController()
        
        return render_template('index.html', title='DicePy - Index')

    ''' Blueprint Imports and Registration '''

    from dicepy.modules.addresses import addresses_bp
    app.register_blueprint(addresses_bp)
    app.add_url_rule('/', endpoint='addresses')

    from dicepy.modules.auth import auth_bp
    app.register_blueprint(auth_bp)
    app.add_url_rule('/', endpoint='auth')

    return app
