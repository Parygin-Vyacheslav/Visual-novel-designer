from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

def blob_to_qp(blob, width=None, height=None):
    qpixmap = QPixmap(width, height)
    if blob:
        qpixmap.loadFromData(blob)
    else:
        qpixmap.fill(Qt.GlobalColor.white)
    return qpixmap