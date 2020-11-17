class UserModel():

    def __init__(self, first_name, last_name, email, phone, username, password, street_address, city, postal_code, province, country):
        self._id = None
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._username = username
        self._password = password
        self._street_address = street_address
        self._city = city
        self._postal_code = postal_code
        self._province = province
        self._country = country
        self._created_at = None

    ''' Properties '''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

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

    ''' Class Methods '''

    # Returns user as dictionary
    def to_dict(self):
        user_dict = {
            'id': self._id,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'email': self._email,
            'phone': self._phone,
            'username': self._username,
            'password': self._password,
            'address_id': self._address_id,
            'created_at': self._created_at
        }
        return user_dict
