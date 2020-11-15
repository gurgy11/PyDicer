from flask import current_app, session, redirect, url_for, wrappers
from flask.globals import request
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        
