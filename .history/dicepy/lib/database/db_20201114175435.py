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

    def insert(self, table, columns, values):
        query_str = """INSERT INTO {table} (""".format(table=table)

        for col in columns:
            col_str = """{col_name}""".format(col_name=col)

            if columns.index(col) == len(columns) - 1:
                col_str += """) """
            else:
                col_str += """, """

            query_str += col_str

        query_str += """VALUES ("""

        for val in values:
            val_str = """%s"""

            if values.index(val) == len(values) - 1:
                val_str += """) """
            else:
                val_str += """, """

            query_str += val_str

        print('Constructed SQL insert statement: ' + query_str)

        cursor = self.cursor()
        cursor.execute(query_str, values)
