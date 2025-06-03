from utility.convert import blob_to_qp
from utility.observer import Observable



class Novel(Observable):
    def __init__(self, id, name, blob_cover):
        '''### Инициализация "приватных" полей
        self._id = None
        self._name
        self._blob_cover
        self._cover'''
        self.observers = []

        # Инициализация "публичных" полей
        self.id = id
        self.name = name
        self.blob_cover = blob_cover
        self.cover = blob_to_qp(blob_cover)
    
    # Инкапсуляция "приватных" полей
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
        self.notify_observers()
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        self.notify_observers()
    
    @property
    def blob_cover(self):
        return self._blob_cover
    @blob_cover.setter
    def blob_cover(self, value):
        self._blob_cover = value
    
    @property
    def cover(self):
        return self._cover
    @cover.setter
    def cover(self, value):
        self._cover = value