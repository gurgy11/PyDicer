from flask import Blueprint, request, render_template, redirect, url_for, jsonify, session, current_app, g

bp = Blueprint('addresses', __name__)


''' INDEX '''
def index():
    addresses = []
    return render_template('addresses/index.html', title='DicePy - Addresses Index', addresses=addresses)
