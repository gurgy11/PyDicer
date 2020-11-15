from mysql.connector import connect
from dicepy.lib.database import Database
from dicepy.modules.users import UserModel


class UsersController():

    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = [
            'first_name', 'last_name', 'email', 'phone', 'username', 'password', 'address_id'
        ]

    ''' Conversion Methods '''
    def form_to_model(self, form):
        user = UserModel(
            form['first_name'],
            form['last_name'],
            form['email'],
            form['phone'],
            form['username'],
            form['password'],
            form['address_id']
        )
        
        return user

    ''' Select '''

    ''' Create and Update '''

    ''' Delete '''
