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
    
    ''' Create Table Methods '''
    
    def create_table(self, schema_sql):
        try:
            cursor = self.cursor()
            cursor.execute(schema_sql)
        
            conn = self.connection
            conn.commit()
        except Exception as e:
            print(str(e))
        # table_str = """CREATE TABLE IF NOT EXISTS {table} (""".format(table=name)
        
        # for col in columns:
        #     table_str += """{column},""".format(column=col)
        
        # table_str += primary_key
        
        # if foreign_keys is not None:
        #     for fk in foreign_keys:
        #         fk_str = """{fk}""".format(fk=fk)
                
        #         if foreign_keys.index(fk) == len(foreign_keys) - 1:
        #             fk_str += ")"
        #         else:
        #             fk_str += ", "
                
        #         table_str += fk_str
                
        # table_str += ")"
        
        # cursor = self.cursor()
        # cursor.execute(table_str)
        
        # conn = self.connection
        # conn.commit()

    ''' Query Execution Methods '''

    def select_all(self, table):
        query_str = """SELECT * FROM {table} """.format(table=table)

        cursor = self.cursor()
        cursor.execute(query_str)

        results = cursor.fetchall()

        data = []
        for res in results:
            data.append(res)

        return data

    def select_by_id(self, table, row_id):
        query_str = """ SELECT * FROM {table} WHERE id = {row_id} """.format(table=table, row_id=row_id)

        cursor = self.cursor()
        cursor.execute(query_str)

        results = cursor.fetchall()

        data = results[0]

        return data

    def select_where_cond(self, table, column, value):
        query_str = """ SELECT * FROM {table} WHERE {column} = "{value}" """.format(
            table=table, column=column, value=value)

        cursor = self.cursor()
        cursor.execute(query_str)

        results = cursor.fetchall()

        data = []
        for res in results:
            data.append(res)

        return data

    def insert(self, table, columns, values):
        query_str = """INSERT INTO {table} (""".format(table=table)

        for col in columns:
            col_str = col

            if columns.index(col) == len(columns) - 1:
                col_str += ") "
            else:
                col_str += ", "

            query_str += col_str

        query_str += "VALUES ("

        for val in values:
            val_str = "%s"

            if values.index(val) == len(values) - 1:
                val_str += ") "
            else:
                val_str += ", "

            query_str += val_str

        print('Constructed SQL insert statement: ' + query_str)

        cursor = self.cursor()
        cursor.execute(query_str, values)

        conn = self.connection
        conn.commit()

        # Todo-> Log result

        return cursor.lastrowid
    
    def number_of_rows(self, table):
        query_str = """SELECT COUNT(*) FROM {table};""".format(table=table)
        
        cursor = self.cursor()
        cursor.execute(query_str)
        
        result = cursor.fetchone()
        num_rows = result[0]
        
        return num_rows

    def update(self, table, columns, values, row_id):
        query_str = """UPDATE `{table}` SET """.format(table=table)
        
        for col in columns:
            col_str = """{col}=%s""".format(col=col)
            
            if columns.index(col) == len(columns) - 1:
                col_str += " "
            else:
                col_str += ", "
                
            query_str += col_str
            
        query_str += """WHERE id={row_id}""".format(row_id=int(row_id))
        
        print(query_str)
        
        cursor = self.cursor()
        cursor.execute(query_str, values)
        
        conn = self.connection
        conn.commit()
        
    def delete(self, table, row_id):
        query_str = """DELETE FROM {table} WHERE id={row_id}""".format(table=table, row_id=row_id)
        
        cursor = self.cursor()
        cursor.execute(query_str)
        
        conn = self.connection
        conn.commit()
        