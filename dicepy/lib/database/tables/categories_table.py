from .table import Table
from ..db import Database


class CategoriesTable(Table):
    
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.table_name = 'categories'
        self.columns = [
            'id',
            'name',
            'description',
            'notes',
            'created_at'
        ]
        self.schema = """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        schema = self.schema
        self.db.create_table(schema)