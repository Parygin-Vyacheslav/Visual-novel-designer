from PyQt6.QtCore import QObject
from abc import ABCMeta

class ViewMeta(type(QObject), ABCMeta): pass