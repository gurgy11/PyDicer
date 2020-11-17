from flask import Blueprint, request, render_template, redirect, url_for, jsonify, session
from dicepy.lib.middleware.auth_middleware import login_required
from . import SuppliersController

bp = Blueprint('suppliers', __name__)

controller = SuppliersController()


@bp.route('/suppliers')
@bp.route('/suppliers/index')
@login_required
def index():
    return render_template('suppliers/index.html', title='Suppliers Index', suppliers=[])


@bp.route('/suppliers/create', methods=['GET', 'POST'])
@login_required
def create():
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
        
        errors = controller.create(form_data)
        if len(errors) > 0:
            return render_template('suppliers/create.html', title='Create a Supplier', errors=errors)
        else:
            return redirect(url_for('suppliers.index'))
    
    return render_template('suppliers/create.html', title='Create a Supplier')


@bp.route('/suppliers/edit/<supplier_id>', methods=['GET', 'POST'])
@login_required
def edit(supplier_id):
    s_id = supplier_id
    supplier = controller.select_by_id(s_id)
    
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
        
        errors = controller.edit(form_data, s_id)
        
        if len(errors) > 0:
            return render_template('suppliers/edit.html', title='Edit Selected Supplier', supplier=supplier, errors=errors)
        else:
            return redirect(url_for('suppliers.index'))
    
    return render_template('suppliers/edit.html', title='Edit Selected Supplier', supplier=supplier)


@bp.route('/suppliers/delete/<supplier_id>')
@login_required
def delete(supplier_id):
    s_id = supplier_id
    supplier = controller.delete(s_id)
    
    return redirect(url_for('suppliers.index'))