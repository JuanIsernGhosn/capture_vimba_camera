# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 964)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1292, 964))
        self.main_view = QVideoLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_view.sizePolicy().hasHeightForWidth())
        self.main_view.setSizePolicy(sizePolicy)
        self.main_view.setMinimumSize(QtCore.QSize(1292, 964))
        self.main_view.setObjectName("main_view")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 22))
        self.menubar.setObjectName("menubar")
        self.menuGrabaci_n = QtWidgets.QMenu(self.menubar)
        self.menuGrabaci_n.setObjectName("menuGrabaci_n")
        MainWindow.setMenuBar(self.menubar)
        self.actionParar = QtWidgets.QAction(MainWindow)
        self.actionParar.setObjectName("actionParar")
        self.actionIniciar = QtWidgets.QAction(MainWindow)
        self.actionIniciar.setObjectName("actionIniciar")
        self.menuGrabaci_n.addSeparator()
        self.menuGrabaci_n.addSeparator()
        self.menuGrabaci_n.addAction(self.actionParar)
        self.menuGrabaci_n.addAction(self.actionIniciar)
        self.menubar.addAction(self.menuGrabaci_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vimba Viewer"))
        self.menuGrabaci_n.setTitle(_translate("MainWindow", "Grabación"))
        self.actionParar.setText(_translate("MainWindow", "Iniciar"))
        self.actionIniciar.setText(_translate("MainWindow", "Parar"))

from view.customwidgets import QVideoLabel

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

