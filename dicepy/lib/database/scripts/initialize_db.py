from dicepy.lib.database.tables import suppliers_table
from ..db import Database
from ..tables import AddressesTable, UsersTable, CategoriesTable, ClientsTable, SuppliersTable

''' Database '''
db = Database()

''' Tables '''
addresses_table = AddressesTable()
users_table = UsersTable()
categories_table = CategoriesTable()
clients_table = ClientsTable()
suppliers_table = SuppliersTable()

''' Create Tables '''
addresses_table.create_table()
users_table.create_table()
categories_table.create_table()
clients_table.create_table()
suppliers_table.create_table()