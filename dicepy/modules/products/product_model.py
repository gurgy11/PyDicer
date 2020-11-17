class ProductModel():
    
    def __init__(self, name, category, description, attributes, sku, upc, in_stock, min_stock, max_stock, 
                 cost_per_unit, price_per_unit, active, storage_location, weight, dimensions, notes):
        self._id = None
        self._name = name
        self._category = category
        self._description = description
        self._attributes = attributes
        self._sku = sku
        self._upc = upc
        self._in_stock = in_stock
        self._min_stock = min_stock
        self._max_stock = max_stock
        self._cost_per_unit = cost_per_unit
        self._price_per_unit = price_per_unit
        self._active = active
        self._storage_location = storage_location
        self._weight = weight
        self._dimensions = dimensions
        self._notes = notes
        self._created_at = None