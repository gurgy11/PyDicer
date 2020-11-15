from flask import Blueprint, request, render_template, redirect, url_for, session, current_app, g

bp = Blueprint('auth', __name__)


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Form data
        form_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm_password')
        }

    return render_template('auth/register.html', title='DicePy - Register')
