from flask import Blueprint, request, render_template, redirect, url_for, session, current_app, g

from dicepy.modules.addresses import AddressesController
from dicepy.modules.users import UsersController

bp = Blueprint('auth', __name__)

a_controller = AddressesController()
u_controller = UsersController()


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Request form's address data
        address_form_data = {
            'street_address': request.form.get('street_address'),
            'city': request.form.get('city'),
            'postal_code': request.form.get('postal_code'),
            'province': request.form.get('province'),
            'country': request.form.get('country')
        }

        # Create new address
        address_id = a_controller.create(address_form_data)

        if address_id is None:
            errors = ['There are problems with the address values. Could not add the address!']
            return render_template('auth/register.html', title='DicePy - Register', errors=errors)

        # Request form's user data
        user_form_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm_password'),
            'address_id': address_id
        }

        # Create new user
        user_created, user_id, errors = u_controller.register(user_form_data)

        if user_created is not True or len(errors) > 0:
            return render_template('auth/register.html', title='DicePy - Register', errors=errors)
        else:
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title='DicePy - Register')


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    request_error = request.args.get('errors')
    if len(request_error) > 0:
        return render_template('auth/login.html', title='DicePy - Login', error=request_error)

    if request.method == 'POST':
        # User form data
        user_form_data = {
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }

        # Login
        errors = u_controller.login(user_form_data)

        if len(errors) > 0:
            return render_template('auth/login.html', title='DicePy - Login', errors=errors)
        else:
            return redirect(url_for('index'))

    return render_template('auth/login.html', title='DicePy - Login')

@bp.route('/auth/login_required')
def login_required():
    error = 'You must be logged into your account to view the requested page!'
    return redirect(url_for('auth.login', errors=[error]))

@bp.route('/auth/logout')
def logout():
    u_controller.logout()
    return redirect(url_for('auth.login'))
