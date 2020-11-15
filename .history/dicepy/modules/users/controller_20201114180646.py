from mysql.connector import connect
from dicepy.lib.database import Database


class UsersController():

    def __init__(self):
        self.db = Database()
