class CategoryModel():
    
    def __init__(self, name, description, notes):
        self._id = None
        self._name = name
        self._description = description
        self._notes = notes
        self._created_at = None
        
    ''' Properties and Setters '''
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
        
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, notes):
        self._notes = notes
        
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
        
    ''' Class Methods '''
    
    def to_dict(self):
        categories_dict = {
            'id': self._id,
            'name': self._name,
            'description': self._description,
            'notes': self._notes,
            'created_at': self._created_at
        }
        
        return categories_dict