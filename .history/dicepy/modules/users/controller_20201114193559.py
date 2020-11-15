from werkzeug.security import check_password_hash, generate_password_hash
from dicepy.lib.database import Database
from ..auth import AuthController
from ..users import UserModel


class UsersController():

    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = [
            'first_name', 'last_name', 'email', 'phone', 'username', 'password', 'address_id'
        ]
        self.auth_controller = AuthController()

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
        values = (user.first_name, user.last_name, user.email,
                  user.phone, user.username, generate_password_hash(user.password), user.address_id)

        return values

    def result_to_model(self, result):
        user = UserModel(result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        user.id = result[0]
        user.created_at = result[8]

        return user

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

    def password_valid(self, hash_password, password):
        password_valid = False

        if check_password_hash(hash_password, password) is True:
            password_valid = True
        
        return password_valid

    def register(self, form):
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

        if len(errors) > 0:
            return False, None, errors

        try:
            user_id = self.db.insert(self.table, self.columns, values)
            print('A new user was successfully created: ' + values)

            return True, user_id, errors
        except Exception as e:
            print('Exceptin throw while creating user: ' + e)
            errors.append(e)

            return False, None, errors

    def login(self, form):
        # User form data
        username = form['username']
        password = form['password']

        errors = []

        # Fetch result with matching username
        results = self.db.select_where_cond(self.table, 'username', username)
        if len(results) > 0:
            user_result = results[0]
            user = self.result_to_model(user_result)

            # Check if password field provided matches password in database
            if self.password_valid(user.password, password) is not True:
                error = 'The password field provided is incorrect!'
                errors.append(error)
            else:
                self.auth_controller.add_user_session_values(user.id, user.username)
        else:
            error = 'The username field provided does not exist!'
            errors.append(error)

        return errors

    def logout(self):
        self.auth_controller.remove_user_session_values()
