class UserModel():

    def __init__(self, first_name, last_name, email, phone, username, password, address_id):
        self._id = None
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._username = username
        self._password = password
        self._address_id = address_id
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
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        self._address_id = address_id

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
