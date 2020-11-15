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
