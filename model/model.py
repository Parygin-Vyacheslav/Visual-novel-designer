import sqlite3
from urllib.request import pathname2url
from abc import ABCMeta, abstractmethod
from utility.observer import Observable

class Model(Observable, metaclass=ABCMeta):
    db = 'file:{}?mode=rw'.format(pathname2url('db/database.db'))
    connection = sqlite3.connect(db, uri=True)
    modified_for_insert = []
    modified_for_update = []
    
    @abstractmethod
    def create(self): # Создания объекта в таблице
        pass

    @abstractmethod
    def update(self): # Изменение объекта в таблице
        pass

    @abstractmethod
    def delete(self): # Удаление объекта из таблицы
        pass