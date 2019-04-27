# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAndTree.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(130, 110, 201, 241))
        self.treeWidget.setObjectName("treeWidget")

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "tree"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "first"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "length"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "width"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "second"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "length"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "width"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print("you press the Esc!")
           # self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.setupUi(w)
    w.show()

    sys.exit(app.exec_())