import math
from dicepy.lib.database import Database
from .supplier_model import SupplierModel


class SuppliersController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'suppliers'
        self.columns = [
            'company_name',
            'description',
            'email',
            'phone',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country'
        ]
        
    ''' Conversion Methods '''
    
    def form_to_model(self, form):
        supplier = SupplierModel(
            form.get('company_name'),
            form.get('description'),
            form.get('email'),
            form.get('phone'),
            form.get('street_address'),
            form.get('city'),
            form.get('postal_code'),
            form.get('province'),
            form.get('country')
        )
        
        return supplier
    
    def form_to_values(self, form):
        supplier = self.form_to_model(form)
        values = (
            supplier.company_name, supplier.description,
            supplier.email, supplier.phone,
            supplier.street_address, supplier.city,
            supplier.postal_code, supplier.province,
            supplier.country
        )
        return values
    
    def result_to_model(self, result):
        res = result
        
        supplier = SupplierModel(
            res[1], res[2], res[3], res[4], res[5], res[6], 
            res[7], res[8], res[9]
        )
        
        supplier.id = res[0]
        supplier.created_at = res[10]
        
        return supplier
    
    ''' Validation Methods '''
    
    def company_name_valid(self, company_name):
        valid_name = False
        
        results = self.db.select_where_cond(self.table, 'company_name', company_name)
        
        if len(results) < 2:
            valid_name = True
        
        return valid_name
    
    def company_name_exists(self, company_name):
        name_exists = False
        results = self.db.select_where_cond(self.table, 'company_name', company_name)
        
        if len(results) > 0:
            name_exists = True
            
        return name_exists
    
    ''' Select Methods '''
    
    def select_all(self):
        results = self.db.select_all(self.table)
        
        suppliers = []
        for res in results:
            supplier = self.result_to_model(res)
            suppliers.append(supplier)
            
        return suppliers
    
    def select_by_id(self, supplier_id):
        result = self.db.select_by_id(self.table, supplier_id)
        supplier = self.result_to_model(result)
        
        return supplier
    
    def select_in_range(self, page, limit):
        start_index = self.get_start_index(page, limit)
        end_index = self.get_end_index(page, limit)
        
        suppliers = self.select_all()
        suppliers_in_range = []
        
        in_range = False
        for s in suppliers:
            if suppliers.index(s) == end_index:
                break
            elif suppliers.index(s) == start_index:
                in_range = True
            
            if in_range:
                suppliers_in_range.append(s)
        
        return suppliers_in_range
    
    ''' Create and Edit Methods '''
    
    def create(self, form):
        values = self.form_to_values(form)
        errors = []
        
        if self.company_name_exists(form.get('company_name')) is True:
            error = 'The company name provided is already taken.'
            errors.append(error)
            
        if len(errors) <= 0:
            try:
                self.db.insert(self.table, self.columns, values)
                print('Successfully created a new supplier in the database!')
            except Exception as e:
                print('Error creating new supplier: ' + str(e))
                
                error = str(e)
                errors.append(error)
        
        return errors
    
    def edit(self, form, supplier_id):
        values = self.form_to_values(form)
        errors = []
        
        if self.company_name_valid(form.get('company_name')) is not True:
            error = 'The company name provided is already taken.'
            errors.append(error)
            
        if len(errors) <= 0:
            try:
                self.db.update(self.table, self.columns, values, supplier_id)
                print('Successfully update the supplier in the database!')
            except Exception as e:
                error = str(e)
                errors.append(error)
                
                print('Error updating the supplier in database: ' + error)
                
        return errors
    
    ''' Delete Methods '''
    
    def delete(self, supplier_id):
        self.db.delete(self.table, supplier_id)
    
    ''' Indexing Methods '''
    
    def get_start_index(self, page, limit):
        return (page - 1) * limit
    
    def get_end_index(self, page, limit):
        return page * limit
    
    def number_of_rows(self):
        return self.db.number_of_rows(self.table)
    
    def number_of_pages(self, limit):
        return math.ceil(self.number_of_rows() / limit)