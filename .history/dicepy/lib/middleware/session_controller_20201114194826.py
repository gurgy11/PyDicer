from flask import current_app, session, redirect, url_for

def authenticate():
    is_authenticated = False
    with current_app.app_context():
        if 'user_id' in session and 'user_username' in session:
            is_authenticated = True
    return is_authenticated

def login_required():
    is_authenticated = authenticate()
    if is_authenticated is True:
        with current_app.app_context():
            return 
