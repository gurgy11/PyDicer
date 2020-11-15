from mysql.connector import connect
from dicepy.lib.database import Database
from dicepy.modules.users import UserModel


class UsersController():

    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = [
            'first_name', 'last_name', 'email', 'phone', 'username', 'password', 'address_id'
        ]

    ''' Conversion Methods '''

    def form_to_model(self, form):
        user = UserModel(
            form['first_name'],
            form['last_name'],
            form['email'],
            form['phone'],
            form['username'],
            form['password'],
            form['address_id']
        )

        return user

    def form_to_values(self, form):
        user = self.form_to_model(form)
        values = (user.first_name, user.last_name, user.email, user.phone, user.username, user.password, user.address_id)

        return values

    ''' Select '''

    ''' Validation '''

    def username_unique(self, username):
        results = self.db.select_where_cond(self.table, 'username', username)
        username_unique = False

        if len(results) <= 0:
            username_unique = True

        return username_unique

    def email_unique(self, email):
        results = self.db.select_where_cond(self.table, 'email', email)
        email_unique = False

        if len(results) <= 0:
            email_unique = True

        return email_unique


    ''' Create and Update '''

    def create(self, form):
        values = self.form_to_values(form)
        
        ### VALIDATION ###

        errors = []

        # Check if passwords match
        if form['password'] != form['confirm_password']:
            error = 'The password fields provided do not match!'
            errors.append(error)

        # Check if username does not already exist
        if self.username_unique(form['username']) is not True:
            error = 'The username field provided is already in use!'
            errors.append(error)

        # Check if email does not already exist
        if self.email_unique(form['email']) is not True:
            error = 'The email field provided is already in use!'
            errors.append(error)

    ''' Delete '''
