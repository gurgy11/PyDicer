import os

from flask import Flask, render_template
from dotenv import load_dotenv

# Local imports
from .settings import *

# Load environment variables
load_dotenv()

def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY
    )
