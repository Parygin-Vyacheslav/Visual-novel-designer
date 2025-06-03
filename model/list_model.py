import sqlite3
from urllib.request import pathname2url
from abc import ABCMeta, abstractmethod
from utility.observer import Observable

class ListModel(Observable, metaclass=ABCMeta):
    db = 'file:{}?mode=rw'.format(pathname2url('db/database.db'))
    connection = sqlite3.connect(db, uri=True)

    @abstractmethod
    def select_all(self): # Извлечение всех записей таблицы
        pass