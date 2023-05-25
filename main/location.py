class Location():

    def __init__(self, country, city, state, postal_code, region):
        self._country = country
        self._city = city
        self._state = state
        self._postal_code = postal_code 
        self._region = region 

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country 

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state 

    @property
    def postal_code(self):
        return self._postal_code
    
    @postal_code.setter
    def posta_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        self._region = region

    def __str__(self) -> str:
        
        description = f'Country: {self._country} - City: {self._city} - State: {self._state} - Postal Code: {self._postal_code} - Region: {self.region}'
        return description