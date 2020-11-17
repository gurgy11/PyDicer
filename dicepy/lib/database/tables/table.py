from ..db_params import db_params


class Table():
    """ A template class for the tables """

    def __init__(self):
        """ Constructor """
        self.db_name = db_params.get('database')  # Use super for db_name

        self.table_name = None
        self.column_names = None
        self.column_expressions = None
        self.primary_key = None
        self.foreign_keys = None

    def create_table(self):
        """ A method that creates the table (if it doesn't already exist') based on the constructor's parameters """
        pass

    def delete_table(self):
        """ A method that deletes the table """
        pass

    def alter_table(self, table_name=None, column_names=None, column_expressions=None, primary_key=None, 
                    foreign_keys=None):
        """ A method to alter the table with new values """
        pass
