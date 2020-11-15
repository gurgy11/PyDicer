from flask import current_app, g, session


class AuthController():

    def __init__(self, user_id, user_username):
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

    # Clears the user's session variables essentially logging them out
    def session_remove_user_params(self):
        with current_app.app_context():
            if 'user_id' in session:
                session.pop('user_id')
            if 'user_username' in session:
                session.pop('user_username')

    # Returns a dictionary of the current authenticated user's session variables
    def session_add_user_params(self):
        with current_app.app_context():
            user_id = session.get('user_id')
            user_username = session.get('user_username')

            user_params = {
                'user_id': user_id,
                'user_username': user_username
            }

            return user_params
