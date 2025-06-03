from utility.observer import Observer



class Replica(Observer):
    def __init__(self, id, text, number, persona):
        self.id = id
        self.text = text
        self.number = number
        self.persona = persona
    
    def update(self):
        id = self.observable.id
        name = self.observable.name
        self.persona = id if id else name
        print(f'{self.name}: my parent is {self.persona}')

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        self._text = value

    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, value):
        self._number = value