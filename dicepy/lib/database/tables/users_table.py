from .table import Table
from ..db import Database


class UsersTable(Table):
    
    def __init__(self):
        super().__init__()
        
        self.db = Database()
        self.table_name = 'users'
        self.columns = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'username',
            'password',
            'address_id',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country',
            'created_at'
        ]
        
        self.schema_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            street_address VARCHAR(255) NOT NULL,
            city VARCHAR(100) NOT NULL,
            postal_code VARCHAR(20) NOT NULL,
            province VARCHAR(100) NOT NULL,
            country VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        schema_sql = self.schema_sql
        self.db.create_table(schema_sql)
        