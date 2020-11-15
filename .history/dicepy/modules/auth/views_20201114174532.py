from flask import Blueprint, request, render_template, redirect, url_for, session, current_app, g

bp = Blueprint('auth', __name__)


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Request form's user data
        user_form_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm_password')
        }

        # Request form's address data
        address_form_data = {
            'street_address': request.form.get('street_address'),
            'city': request.form.get('city'),
            'postal_code': request.form.get('postal_code'),
            'province': request.form.get('province'),
            'country': request.form.get('country')
        }

    return render_template('auth/register.html', title='DicePy - Register')
