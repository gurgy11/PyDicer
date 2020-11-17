from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from dicepy.lib.middleware.auth_middleware import login_required
from . import ClientsController

bp = Blueprint('clients', __name__)

controller = ClientsController()


@bp.route('/clients')
@bp.route('/clients/index')
@login_required
def index():
    return render_template('clients/index.html', title='Clients Index', clients=[])