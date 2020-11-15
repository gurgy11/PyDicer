class AddressModel():

    def __init__(self, street_address, city, postal_code, province, country):
        self._id = None
        self._street_address = street_address
        self._city = city
        self._postal_code = postal_code
        self._province = province
        self._country = country
        self._created_at = None


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, province):
        self._province = province

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
