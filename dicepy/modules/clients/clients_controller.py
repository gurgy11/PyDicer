from dicepy.lib.database import Database


class ClientsController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'clients'
        self.columns = [
            'company_name',
            'description',
            'email',
            'phone',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country',
        ]