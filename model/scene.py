from utility.convert import blob_to_qp
from utility.observer import Observable, Observer

from PyQt6.QtGui import QColor



class Scene(Observable, Observer):
    def __init__(self, id, name, blob_background, width, height, novel):
        self.observers = []
        self.id = id
        self.name = name
        self.blob_background = blob_background
        self.background = blob_to_qp(blob_background, width, height)
        self.width = width
        self.height = height
        self.novel = novel
    
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
    def background(self):
        return self._background
    @background.setter
    def background(self, value):
        self._background = value
        self.notify_observers()
    
    '''@property
    def blob_background(self):
        return self._blob_background
    @blob_background.setter
    def blob_background(self, value):
        self._blob_background = value

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value'''

    def update(self):
        id = self.observable.id
        name = self.observable.name
        self.novel = id if id else name
        print(f'{self.name}: my parent is {self.novel}')
