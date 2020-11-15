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

    def create(self, form):
        pass
