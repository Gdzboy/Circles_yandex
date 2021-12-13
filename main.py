import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Круги')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        n = randrange(150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(60, 100, n, n)
        nu = randrange(150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(300, 100, nu, nu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())