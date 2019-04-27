
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets




if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 800)
    w.move(300, 130)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())