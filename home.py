# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-image: url(:/pic/2.png);\n"
"background-color: rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_red = QtWidgets.QPushButton(self.centralwidget)
        self.button_red.setGeometry(QtCore.QRect(90, 170, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_red.setFont(font)
        self.button_red.setStyleSheet("background: rgb(255, 0, 0);\n"
"font-size: 14pt;\n"
"color:rgb(0, 0, 0)")
        self.button_red.setObjectName("button_red")
        self.button_yellow = QtWidgets.QPushButton(self.centralwidget)
        self.button_yellow.setGeometry(QtCore.QRect(90, 250, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_yellow.setFont(font)
        self.button_yellow.setStyleSheet("background:rgb(255, 255, 0);\n"
"font-size: 14pt ;\n"
"color: rgb(0, 0, 0)")
        self.button_yellow.setObjectName("button_yellow")
        self.button_green = QtWidgets.QPushButton(self.centralwidget)
        self.button_green.setGeometry(QtCore.QRect(90, 330, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_green.setFont(font)
        self.button_green.setStyleSheet("background:rgb(0, 255, 0)")
        self.button_green.setObjectName("button_green")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_red.setText(_translate("MainWindow", "RED"))
        self.button_yellow.setText(_translate("MainWindow", "YELLOW"))
        self.button_green.setText(_translate("MainWindow", "GREEN"))
import picture_rc
