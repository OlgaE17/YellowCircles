import sys
import io
from PyQt6 import uic  
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt, QPointF
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
    
    def run(self):
        self.do_paint = True
        self.update()
    
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            diam = randint(20, 100)
            x = randint(50, 700)
            y = randint(50, 500)
            qp.setBrush(QColor(250, 200, 30))
            qp.drawEllipse(QPointF(x, y), diam, diam)
            qp.end()
         self.do_paint = False      
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
