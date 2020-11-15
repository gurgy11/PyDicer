from dicepy.lib.database import Database
from dicepy.modules.addresses import AddressModel


class AddressesController():

    def __init__(self):
        self.db = Database()
        self.table = 'addresses'
        self.columns = [
            'street_address',
            'city',
            'postal_code',
            'province',
            'country'
        ]

    def form_to_model(self, form):
        address = AddressModel(
            form['street_address'],
            form['city'],
            form['postal_code'],
            form['province'],
            form['country']
        )

        return address

    def form_to_values(self, form):
        address = self.form_to_model(self, form)
        values = (
            address.street_address, address.city, address.postal_code, address.province, address.country
        )

        return values

    def create(self, form):
        values = self.form_to_values(form)
        
        try:
            address_id = self.db.insert(self.table, self.columns, values)
            print('Created new address in database: ' + values)

            return True, address_id
        except Exception as e:
            print('Database or MySQL exception thrown: ' + e)
            
            return False, None
