from flask import Blueprint, request, render_template, redirect, url_for, session, current_app, g

bp = Blueprint('auth', __name__)


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', title='DicePy - Register')
