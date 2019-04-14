# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/dec/Detection/guifinish\guiai.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1022, 681)
        Form.setMaximumSize(QtCore.QSize(16777213, 16777215))
        Form.setStyleSheet("background-color:rgb(255, 243, 175)")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 80, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bangna New")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 134, 136);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 80, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bangna New")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(150, 255, 142);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 121, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 120, 121, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 180, 801, 391))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "STOP"))
        self.pushButton.setText(_translate("Form", "START"))
        self.comboBox.setItemText(0, _translate("Form", "YOLO V3"))
        self.comboBox.setItemText(1, _translate("Form", "RESNET"))
        self.comboBox.setItemText(2, _translate("Form", "YOLO TINY"))
        self.comboBox_2.setItemText(0, _translate("Form", "Person"))
        self.comboBox_2.setItemText(1, _translate("Form", "Car"))
        self.comboBox_2.setItemText(2, _translate("Form", "Cell Phone"))


