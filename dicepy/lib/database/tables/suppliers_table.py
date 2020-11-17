from .table import Table
from ..db import Database


class SuppliersTable(Table):

    def __init__(self):
        super().__init__()
        self.db = Database()
        self.table_name = 'suppliers'
        self.columns = [
            'id',
            'company_name',
            'description',
            'email',
            'phone',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country',
            'created_at'
        ]
        self.schema = """
        CREATE TABLE IF NOT EXISTS suppliers (
            id INT AUTO_INCREMENT,
            company_name VARCHAR(100) NOT NULL,
            description TEXT,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(25) NOT NULL,
            street_address VARCHAR(255) NOT NULL,
            city VARCHAR(100) NOT NULL,
            postal_code VARCHAR(25) NOT NULL,
            province VARCHAR(100) NOT NULL,
            country VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """

    def create_table(self):
        schema = self.schema
        self.db.create_table(schema)
