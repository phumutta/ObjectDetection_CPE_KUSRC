# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/dec/Detection\guiai8.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setMaximumSize(QtCore.QSize(16777213, 16777215))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(3, 219, 172)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(3, 219, 172);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 121, 41))
        self.comboBox.setStyleSheet("background-color: rgb(3, 219, 172)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 180, 121, 41))
        self.comboBox_2.setStyleSheet("background-color: rgb(3, 219, 172)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.graphicsView.setStyleSheet("background: url(D:Object.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 120, 851, 471))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(3, 219, 172);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(1030, 120, 210, 481))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setStyleSheet("background-color: rgb(3, 219, 172);")
        self.listWidget.setIconSize(QtCore.QSize(200, 150))
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.listWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "STOP"))
        self.pushButton_2.setText(_translate("Form", "START"))
        self.comboBox.setItemText(0, _translate("Form", "YOLO V3"))
        self.comboBox.setItemText(1, _translate("Form", "RESNET"))
        self.comboBox.setItemText(2, _translate("Form", "YOLO TINY"))
        self.comboBox_2.setItemText(0, _translate("Form", "Person"))
        self.comboBox_2.setItemText(1, _translate("Form", "Car"))
        self.comboBox_2.setItemText(2, _translate("Form", "Cell Phone"))
        self.comboBox_2.addItems(["Bicycle","Car","Motorcycle","Airplane","Bus","Train","Truck","Boat","Traffic Light","Fire Hydrant","Stop Sign","Giraffe","Backpack","Umbrella","Handbag","Tie","Suitcase","Frisbee"])
        self.comboBox_2.addItems(["Skis","Snowboard","Sports Ball","Kite","Baseball Bat","Baseball Glove","Skateboard","Surfboard","Tennis Rack","Bottle","Wine Glass","Cup","Fork","Knife","Spoon","Bowl","Banana","Apple"])
        self.comboBox_2.addItems(["Sandwich","Broccoli","Carrot","Hot Dog","Pizza","Cake","Chair","Couch","Potted Plant","bed","Dining Table","Toilet","Tv","Laptop","Mouse","Remote","Keyboard","Microwave","Oven","Toaster","Sink"])
        self.comboBox_2.addItems(["Refrigerator","Book","Clock","Vase","Scissors","Teddy Bear","Hair Dryer","Toothbrush"])
        self.comboBox_2.addItems(["Parking Meter","Bench","Bird","Cat","Dog","Horse","Sheep","Cow","Elephant","Bear","Zebra","ALL"])

        self.pushButton_3.setText(_translate("Form", "Capture"))


