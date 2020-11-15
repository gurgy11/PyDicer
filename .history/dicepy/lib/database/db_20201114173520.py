import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()


class Database():

    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    ''' Database Methods '''

    def cursor(self):
        return self.connection.cursor()

    ''' Query Execution Methods '''
