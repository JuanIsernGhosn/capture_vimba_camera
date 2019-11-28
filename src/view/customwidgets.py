from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class QVideoLabel(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            size = self.size()
            painter = QPainter(self)
            point = QPoint(0, 0)
            scaledPix = self.p.scaled(size, Qt.IgnoreAspectRatio, transformMode=Qt.SmoothTransformation)
            self.setMaximumSize(scaledPix.size())
            point.setX(0)
            point.setY(0)
            painter.drawPixmap(point, scaledPix)
            self.setMaximumSize(QSize(4000, 5000))
