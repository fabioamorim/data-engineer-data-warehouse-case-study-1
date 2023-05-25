class Order():

    def __init__(self,row_id, id, date, ship_date, ship_mode, sale):
        self._row_id = row_id
        self._id = id
        self._date = date
        self._ship_date = ship_date
        self._ship_mode = ship_mode
        self._sale = float(sale)
        self._product = None
        self._customer = None 
        self._location = None 


    @property
    def row_id(self):
        return self._row_id 

    @row_id.setter
    def row_id(self, row_id):
        self._row_id = row_id

    @property
    def id(self):
        return self._id 
    
    @id.setter
    def id(self, id):
        self._id = id 

    @property
    def date(self):
        return self._date 
    
    @date.setter
    def date(self, date):
        self._date = date 

    @property
    def ship_date(self):
        return self._ship_date 
    
    @ship_date.setter
    def ship_date(self, ship_date):
        self._ship_date = ship_date
    
    @property
    def ship_mode(self):
        return self._ship_mode 
    
    @ship_mode.setter
    def ship_mode(self, ship_mode):
        self._ship_mode = ship_mode

    @property
    def sale(self):
        return self._sale
    
    @sale.setter
    def sale(self, sale):
        self._sale = sale

    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, product):
        self._product = product

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        self._location = location

    def __str__(self) -> str:
        
        description = f'Row ID: {self._row_id} - Order ID: {self._id} - Order Date: {self._date} \n {self._product} \n {self.customer} \n {self._location}'
        return description