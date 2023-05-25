class Customer():

    def __init__(self, id, name, segment):
        self._id = id
        self._name = name
        self._segment = segment

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
    def segment(self):
        return self._segment
    
    @segment.setter
    def segment(self, segment):
        self._segment = segment

    def __str__(self) -> str:
        
        description = f'Customer ID: {self._id} - Customer Name: {self._name} - Segment: {self._segment}'
        return description