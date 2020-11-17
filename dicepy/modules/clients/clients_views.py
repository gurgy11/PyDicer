from flask import Blueprint, request, render_template, redirect, url_for, jsonify, session
from dicepy.lib.middleware.auth_middleware import login_required
from . import ClientsController

bp = Blueprint('clients', __name__)

controller = ClientsController()


@bp.route('/clients')
@bp.route('/clients/index')
@login_required
def index():
    page = None
    limit = None
    
    if 'page' in request.args:
        page = int(request.args['page'])
    else:
        page = 1
    
    if 'limit' in request.args:
        limit = int(request.args['limit'])
    else:
        limit = 10
        
    session['client_page'] = page
    session['client_limit'] = limit
        
    print('Start Index: ' + str(controller.get_start_index(int(page), int(limit))))
    print('End Index: ' + str(controller.get_end_index(int(page), int(limit))))
    
    clients = controller.select_in_range(page, limit)
    num_pages = controller.number_of_pages(limit)
    
    return render_template('clients/index.html', title='Clients Index', clients=clients, num_pages=num_pages, page=page, limit=limit)


@bp.route('/clients/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Register form data
        form_data = {
            'company_name': request.form.get('company_name'),
            'description': request.form.get('description'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'street_address': request.form.get('street_address'),
            'city': request.form.get('city'),
            'postal_code': request.form.get('postal_code'),
            'province': request.form.get('province'),
            'country': request.form.get('country')
        }
        
        errors = controller.create(form_data)
        
        if len(errors) > 0:
            return render_template('clients/create.html', title='Create a client', errors=errors)
        else:
            return redirect(url_for('clients.index'))
    
    return render_template('clients/create.html', title='Create a client')


@bp.route('/clients/edit/<client_id>', methods=['GET', 'POST'])
@login_required
def edit(client_id):
    c_id = client_id
    client = controller.select_by_id(c_id)
    print(client.company_name)
    
    if request.method == 'POST':
        # Request form data
        form_data = {
            'company_name': request.form.get('company_name'),
            'description': request.form.get('description'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'street_address': request.form.get('street_address'),
            'city': request.form.get('city'),
            'postal_code': request.form.get('postal_code'),
            'province': request.form.get('province'),
            'country': request.form.get('country')
        }
        
        errors = controller.edit(c_id, form_data)
        
        if len(errors) > 0:
            return render_template('clients/edit.html', title='Edit a client', errors=errors)
        else:
            page = session.get('client_page')
            limit = session.get('client_limit')
            return redirect(url_for('clients.index'))
    
    return render_template('clients/edit.html', title='Edit a client', client=client)


@bp.route('/clients/delete/<client_id>')
def delete(client_id):
    c_id = client_id
    controller.delete(c_id)
    
    return redirect(url_for('clients.index'))