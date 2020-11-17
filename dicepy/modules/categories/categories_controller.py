import math
from flask import current_app, g, session, redirect, url_for
from dicepy.lib.database import Database
from . import CategoryModel


class CategoriesController():
    
    def __init__(self):
        self.db = Database()
        self.table_name = 'categories'
        self.columns = [
            'name',
            'description',
            'notes'
        ]
        
    def form_to_model(self, form):
        category = CategoryModel(form.get('name'), form.get('description'), form.get('notes'))
        
        return category
    
    def form_to_values(self, form):
        category = self.form_to_model(form)
        values = (category.name, category.description, category.notes)
        
        return values
    
    def result_to_model(self, result):
        category = CategoryModel(result[1], result[2], result[3])
        category.id = result[0]
        category.created_at = result[4]
        
        return category
    
    def name_exists(self, name):
        results = self.db.select_where_cond(self.table_name, 'name', name)
        
        name_exists = False
        if len(results) > 0:
            name_exists = True
            
        return name_exists
        
    def create(self, form):
        values = self.form_to_values(form)
        errors = []
        
        # Validate name
        if self.name_exists(form.get('name')) is True:
            error = 'The name of the category provided is already being used.'
            errors.append(error)
            
        if len(errors) <= 0:
            category_id = self.db.insert(self.table_name, self.columns, values)
            
            return None
        else:
            return errors
        
    def number_of_rows(self):
        num_rows = self.db.number_of_rows(self.table_name)
        return num_rows
    
    def number_of_pages(self, limit):
        num_rows = self.number_of_rows()
        num_pages = math.ceil(num_rows / limit)
        
        return num_pages
    
    def last_row_index(self):
        num_rows = self.db.number_of_rows(self.table_name)
        last_row_index = num_rows - 1
        
        return last_row_index
    
    def page_index_range(self, page, limit):
        offset = (page - 1) * limit
        return offset
    
    def get_start_index(self, page, limit):
        start_index = int((page - 1) * limit)
        return start_index

    def get_end_index(self, page, limit):
        end_index = int(page * limit)
        return end_index
    
    def select_all(self):
        results = self.db.select_all(self.table_name)
        categories = []
        
        for res in results:
            category = self.result_to_model(res)
            categories.append(category)
            
        return categories
    
    def select_by_id(self, category_id):
        result = self.db.select_by_id(self.table_name, category_id)
        category = self.result_to_model(result)
        
        return category
    
    def select_in_range(self, page, limit):
        start_index = self.get_start_index(page, limit)
        end_index = self.get_end_index(page, limit)
        
        all_categories = self.select_all()
        range_categories = []
        
        in_range = False
        for cat in all_categories:
            if all_categories.index(cat) == end_index:
                break
            if all_categories.index(cat) == start_index:
                in_range = True
            
            if in_range:
                range_categories.append(cat)
                
        return range_categories
    
    def edit(self, category_id, form):
        category = self.form_to_model(form)
        values = self.form_to_values(form)
        errors = None
        
        name_results = self.db.select_where_cond(self.table_name, 'name', category.name)
        if len(name_results) > 1:
            error = 'The name provided is already in use by multiple categories.'
            errors.append(error)
        elif len(name_results) < 2:
            try:
                self.db.update(self.table_name, self.columns, values, category_id)
            except Exception as e:
                print('Exception while updating table row: ' + str(e))
                errors.append(str(e))
        
        return errors
    
    def delete(self, category_id):
        self.db.delete(self.table_name, category_id)