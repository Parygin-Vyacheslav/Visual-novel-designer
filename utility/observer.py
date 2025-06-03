from abc import ABCMeta, abstractmethod

class Observable():
    #observers = [] # Список наблюдателей

    def add_observer(self, observer): # Добваление наблюдателя
        self.observers.append(observer)
        observer.observable = self
    
    def remove_observer(self, observer): # Удаление наблюдателя
        self.observers.remove(observer)

    def notify_observers(self): # Оповещение наблюдателей об изменении
        for observer in self.observers:
            observer.update()


class Observer(metaclass = ABCMeta):
    observable = None

    @abstractmethod
    def update(self):
        pass