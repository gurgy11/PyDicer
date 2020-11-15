from flask import session, redirect, url_for

def authenticate():
    is_authenticated = False
    with current_app.app_context():
        if 'user_id' in session and 'user_username' in session:
            is_authenticated = True
    return is_authenticated

def login_required(current_app):
    is_authenticated = authenticate()
    if is_authenticated is True:
        with current_app.app_context():
            return redirect(url_for('auth.login_required'))
