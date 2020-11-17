from .table import Table
from ..db import Database


class AddressesTable(Table):

    def __init__(self):
        super().__init__()
        self.db = Database()
        self.table_name = 'addresses'
        self.columns = [
            'id',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country',
            'created_at'
        ]
        
        self.schema_sql = """
        CREATE TABLE IF NOT EXISTS addresses (
            id INT AUTO_INCREMENT,
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
        """ Creates the addresses table """
        
        """ table_name = self.table_name
        columns = self.columns
        pk = self.primary_key
        fk = self.foreign_keys
        
        return self.db.create_table(table_name, columns, pk, fk) """
        
        schema_sql = self.schema_sql
        self.db.create_table(schema_sql)
