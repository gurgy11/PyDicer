from flask import current_app, session, redirect, url_for
from flask.globals import request

def authenticate_user(f):
    @wraps(f)
    def login_required(*args, **kwargs)
