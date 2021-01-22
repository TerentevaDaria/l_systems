# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_confirm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout.addWidget(self.pushButton_confirm, 19, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinBox_generation = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_generation.setMaximum(30)
        self.spinBox_generation.setProperty("value", 1)
        self.spinBox_generation.setObjectName("spinBox_generation")
        self.horizontalLayout_6.addWidget(self.spinBox_generation)
        self.gridLayout.addLayout(self.horizontalLayout_6, 18, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_skip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_skip.setObjectName("lineEdit_skip")
        self.horizontalLayout_7.addWidget(self.lineEdit_skip)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 10, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_draw = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_draw.setObjectName("lineEdit_draw")
        self.horizontalLayout_3.addWidget(self.lineEdit_draw)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_direction = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_direction.setObjectName("comboBox_direction")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_direction)
        self.gridLayout.addLayout(self.horizontalLayout_5, 12, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.doubleSpinBox_angle = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_angle.setDecimals(1)
        self.doubleSpinBox_angle.setMaximum(180.0)
        self.doubleSpinBox_angle.setSingleStep(0.1)
        self.doubleSpinBox_angle.setProperty("value", 90.0)
        self.doubleSpinBox_angle.setObjectName("doubleSpinBox_angle")
        self.horizontalLayout.addWidget(self.doubleSpinBox_angle)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_step = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_step.setMinimum(1)
        self.spinBox_step.setMaximum(50)
        self.spinBox_step.setObjectName("spinBox_step")
        self.horizontalLayout_4.addWidget(self.spinBox_step)
        self.gridLayout.addLayout(self.horizontalLayout_4, 17, 0, 1, 1)
        self.lineEdit_axiom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_axiom.setObjectName("lineEdit_axiom")
        self.gridLayout.addWidget(self.lineEdit_axiom, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 18))
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
        self.pushButton_confirm.setText(_translate("MainWindow", "Построить"))
        self.label_4.setText(_translate("MainWindow", "Правила:"))
        self.label_5.setText(_translate("MainWindow", "поколение"))
        self.label_8.setText(_translate("MainWindow", "Пропустить"))
        self.label_7.setText(_translate("MainWindow", "Использовать для рисования"))
        self.label_6.setText(_translate("MainWindow", "направление"))
        self.comboBox_direction.setItemText(0, _translate("MainWindow", "вверх"))
        self.comboBox_direction.setItemText(1, _translate("MainWindow", "вниз"))
        self.comboBox_direction.setItemText(2, _translate("MainWindow", "влево"))
        self.comboBox_direction.setItemText(3, _translate("MainWindow", "вправо"))
        self.label_3.setText(_translate("MainWindow", "Угол"))
        self.label.setText(_translate("MainWindow", "Аксиома:"))
        self.label_2.setText(_translate("MainWindow", "длина шага"))
