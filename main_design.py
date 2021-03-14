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
        MainWindow.resize(563, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_step = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_step.setMinimum(1)
        self.spinBox_step.setMaximum(100)
        self.spinBox_step.setObjectName("spinBox_step")
        self.horizontalLayout_4.addWidget(self.spinBox_step)
        self.gridLayout.addLayout(self.horizontalLayout_4, 15, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_draw = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_draw.setObjectName("lineEdit_draw")
        self.horizontalLayout_3.addWidget(self.lineEdit_draw)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.lineEdit_axiom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_axiom.setObjectName("lineEdit_axiom")
        self.gridLayout.addWidget(self.lineEdit_axiom, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinBox_generation = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_generation.setMaximum(50)
        self.spinBox_generation.setProperty("value", 1)
        self.spinBox_generation.setObjectName("spinBox_generation")
        self.horizontalLayout_6.addWidget(self.spinBox_generation)
        self.gridLayout.addLayout(self.horizontalLayout_6, 16, 0, 1, 1)
        self.pushButton_confirm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout.addWidget(self.pushButton_confirm, 17, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(400, 10, 141, 541))
        self.openGLWidget.setObjectName("openGLWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 18))
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
        self.label_3.setText(_translate("MainWindow", "Угол"))
        self.label_4.setText(_translate("MainWindow", "Правила:"))
        self.label.setText(_translate("MainWindow", "Аксиома:"))
        self.label_2.setText(_translate("MainWindow", "длина шага"))
        self.label_7.setText(_translate("MainWindow", "Использовать для рисования"))
        self.label_5.setText(_translate("MainWindow", "поколение"))
        self.pushButton_confirm.setText(_translate("MainWindow", "Построить"))
