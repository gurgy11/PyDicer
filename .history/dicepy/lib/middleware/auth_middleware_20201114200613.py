from flask import current_app, session, redirect, url_for, wrappers
from flask.globals import request
from functools import wraps

def authenticate_user(f):
    @wraps(f)
    def login_required(*args, **kwargs):
        
