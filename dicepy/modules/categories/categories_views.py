from flask import Blueprint, request, render_template, redirect, url_for, jsonify, request
from dicepy.lib.middleware.auth_middleware import login_required
from . import CategoriesController

bp = Blueprint('categories', __name__)

controller = CategoriesController()


''' Index '''
@bp.route('/categories')
@bp.route('/categories/index')
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
        print(limit)
    else:
        limit = 10
        
    print('Start Index: ' + str(controller.get_start_index(page, limit)))
    print('End Index: ' + str(controller.get_end_index(page, limit)))
    
    categories = controller.select_in_range(page, limit)
    num_pages = controller.number_of_pages(limit)
    
    return render_template('categories/index.html', title='Categories Index', categories=categories, num_pages=num_pages, page=page, limit=limit)


''' Create '''
@bp.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Request form data
        form_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'note': request.form.get('note')
        }
        
        errors = controller.create(form_data)
        
        if errors is None:
            return redirect(url_for('categories.index'))
        else:
            return render_template('categories/create.html', title='Create New Category', errors=errors)
    
    return render_template('categories/create.html', title='Create New Category')


''' Edit '''
@bp.route('/categories/edit/<category_id>', methods=['GET', 'POST'])
@login_required
def edit(category_id):
    category_id = int(category_id)
    category = controller.select_by_id(category_id)
    
    if request.method == 'POST':
        # Request form data
        form_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'notes': request.form.get('notes')
        }
        
        errors = controller.edit(category_id, form_data)
        
        if errors is not None and len(errors) > 0:
            return render_template('categories/create.html', title='Edit a category', errors=errors)
        else:
            return redirect(url_for('categories.index'))
    
    return render_template('categories/edit.html', title='Edit Category', category=category)


''' Delete '''
@bp.route('/categories/delete/<category_id>')
@login_required
def delete(category_id):
    c_id = int(category_id)
    controller.delete(c_id)
    
    return redirect(url_for('categories.index'))