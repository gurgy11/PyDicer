from flask import current_app, g, session, redirect, url_for
from flask.helpers import url_for


class AuthController():

    def __init__(self, user_id=None, user_username=None):
        self._user_id = user_id
        self._user_username = user_username

    @property
    def user_id(self):
        return self._user_id

    @property
    def user_username(self):
        return self._user_username

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @user_username.setter
    def user_username(self, user_username):
        self._user_username = user_username

    # Adds the user sesssion variables, logging the user in
    def add_user_session_values(self, user_id, user_username):
        with current_app.app_context():
            session['user_id'] = user_id
            session['user_username'] = user_username

    # Clears the user's session variables essentially logging them out
    def remove_user_session_values(self):
        with current_app.app_context():
            if 'user_id' in session:
                session.pop('user_id')
            if 'user_username' in session:
                session.pop('user_username')

    # Returns a dictionary of the current authenticated user's session variables
    def get_user_session_values(self):
        with current_app.app_context():
            user_id = session.get('user_id')
            user_username = session.get('user_username')

            user_params = {
                'user_id': user_id,
                'user_username': user_username
            }

            return user_params

    # Checks if the user is in session and returns a bool
    def authenticate(self):
        with current_app.app_context():
            authenticated = False

            if 'user_id' in session and 'user_username' in session:
                authenticated = True

            return authenticated

    # Protects a page that requires the user to be logged in
    def login_required(self):
        authenticated = self.authenticate()

        with current_app.app_context():
            if authenticated is not True:
                return redirect(url_for('auth.login_required'))
