from utility.convert import blob_to_qp
from utility.observer import Observable, Observer



class Persona(Observable, Observer):
    def __init__(self, id, name, blob_skin, scene):
        self.observers = []
        self.id = id
        self.name = name
        self.blob_skin = blob_skin
        self.skin = blob_to_qp(blob_skin)
        self.scene = scene

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
    def blob_skin(self):
        return self._blob_skin
    @blob_skin.setter
    def blob_skin(self, value):
        self._blob_skin = value

    @property
    def skin(self):
        return self._skin
    @skin.setter
    def skin(self, value):
        self._skin = value
    
    def update(self):
        id = self.observable.id
        name = self.observable.name
        self.scene = id if id else name
        print(f'{self.name}: my parent is {self.scene}')