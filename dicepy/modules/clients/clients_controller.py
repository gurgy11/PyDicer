import math
from dicepy.lib.database import Database
from .client_model import ClientModel


class ClientsController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'clients'
        self.columns = [
            'company_name',
            'description',
            'email',
            'phone',
            'street_address',
            'city',
            'postal_code',
            'province',
            'country',
        ]
        
    def form_to_model(self, form):
        client = ClientModel(form.get('company_name'), form.get('description'), form.get('email'), form.get('phone'), form.get('street_address'), 
                             form.get('city'), form.get('postal_code'), form.get('province'), form.get('country'))
        
        return client
    
    def form_to_values(self, form):
        client = self.form_to_model(form)
        values = (client.company_name, client.description, client.email, client.phone, client.street_address, client.city, client.postal_code, 
                  client.province, client.country)
        
        return values
    
    def result_to_model(self, result):
        client = ClientModel(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
        client.id = result[0]
        client.created_at = result[10]
        
        return client
    
    def company_name_exists(self, company_name):
        results = self.db.select_where_cond(self.table, 'company_name', company_name)
        name_exists = False
        
        if len(results) > 0:
            name_exists = True
            
        return name_exists
    
    def validate_company_name(self, company_name):
        results = self.db.select_where_cond(self.table, 'company_name', company_name)
        clients = []
        
        for res in results:
            client = self.result_to_model(res)
            clients.append(client)
        
        num_matches = len(clients)
        
        valid_company = False
        
        if num_matches < 2:
            valid_company = True
            
        return valid_company
    
    def select_all(self):
        results = self.db.select_all(self.table)
        clients = []
        
        for res in results:
            client = self.result_to_model(res)
            clients.append(client)
            
        return clients
    
    def select_by_id(self, client_id):
        result = self.db.select_by_id(self.table, client_id)
        client = self.result_to_model(result)
        
        return client
    
    def create(self, form):
        values = self.form_to_values(form)
        errors = []
        
        # Check if company name already exists
        if self.company_name_exists(form['company_name']) is True:
            error = 'The company name provided is already taken.'
            errors.append(error)
            
        if len(errors) <= 0:
            client_id = self.db.insert(self.table, self.columns, values)
        
        return errors
    
    def get_start_index(self, page, limit):
        start_index = int((page - 1) * limit)
        return start_index
    
    def get_end_index(self, page, limit):
        end_index = page * limit
        return end_index
    
    def number_of_rows(self):
        num_rows = self.db.number_of_rows(self.table)
        return num_rows
    
    def number_of_pages(self, limit):
        num_rows = self.number_of_rows()
        num_pages = math.ceil(num_rows / limit)
        
        return num_pages
    
    def select_in_range(self, page, limit):
        start_index = self.get_start_index(page, limit)
        end_index = self.get_end_index(page, limit)
        
        all_clients = self.select_all()
        range_clients = []
        
        in_range = False
        for client in all_clients:
            if all_clients.index(client) == end_index:
                break
            if all_clients.index(client) == start_index:
                in_range = True
            
            if in_range:
                range_clients.append(client)
                
        return range_clients
    
    def edit(self, client_id, form):
        values = self.form_to_values(form)
        errors = []
        
        # Validate company name
        valid_name = self.validate_company_name(form.get('company_name'))
        if valid_name is not True:
            error = 'The company name provided is already taken.'
            errors.append(error)
            
        if len(errors) <= 0:
            try:
                self.db.update(self.table, self.columns, values, client_id)
            except Exception as e:
                error = str(e)
                errors.append(error)
            
        return errors
    
    def delete(self, client_id):
        self.db.delete(self.table, client_id)