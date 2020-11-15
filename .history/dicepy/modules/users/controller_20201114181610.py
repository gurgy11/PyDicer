from mysql.connector import connect
from dicepy.lib.database import Database


class UsersController():

    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = [
            'first_name', 'last_name', 'email', 'phone', 'username', 'password', 'address_id'
        ]

    ''' Conversion Methods '''

    ''' Select '''

    ''' Create and Update '''

    ''' Delete '''
