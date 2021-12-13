import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from random import randrange, randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Круги')
        self.btn = QPushButton('Нажмите', self)
        self.btn.resize(100, 100)
        self.btn.move(275, 325)
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
        qp.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
        qp.drawEllipse(60, 100, n, n)
        nu = randrange(150)
        qp.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
        qp.drawEllipse(300, 100, nu, nu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
