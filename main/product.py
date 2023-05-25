class Product():

    def __init__(self, id, name, category, sub_category):
        self._id = id
        self._name = name
        self._category = category
        self._sub_category = sub_category

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
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category

    @property
    def sub_category(self):
        return self._sub_category
    
    @sub_category.setter
    def sub_category(self, sub_category):
        self._sub_category = sub_category

    def __str__(self) -> str:
        
        description = f'Production ID: {self._id} - Production Name: {self._name} - Category: {self._category} - Sub-Category: {self._sub_category}'
        return description