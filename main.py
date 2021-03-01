import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
#asd

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gr = uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.update_picture)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor('yellow'))
            qp.setBrush(QColor('yellow'))
            a = randint(3, 250)
            qp.drawEllipse((800 - a) // 2, 300, a, a)
            qp.end()
            self.do_paint = False

    def update_picture(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
