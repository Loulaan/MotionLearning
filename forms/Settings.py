# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(651, 400)
        TabWidget.setMinimumSize(QtCore.QSize(363, 224))
        TabWidget.setMaximumSize(QtCore.QSize(680, 400))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.vRBf_1 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_1.setObjectName("vRBf_1")
        self.verticalLayout.addWidget(self.vRBf_1)

        self.vRBf_2 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_2.setObjectName("vRBf_2")
        self.verticalLayout.addWidget(self.vRBf_2)

        self.vRBf_3 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_3.setObjectName("vRBf_3")
        self.verticalLayout.addWidget(self.vRBf_3)

        self.vRBf_4 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_4.setObjectName("vRBf_4")
        self.verticalLayout.addWidget(self.vRBf_4)

        self.vRBf_5 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_5.setObjectName("vRBf_5")
        self.verticalLayout.addWidget(self.vRBf_5)

        self.vRBf_6 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_6.setObjectName("vRBf_6")
        self.verticalLayout.addWidget(self.vRBf_6)

        self.vRBf_7 = QtWidgets.QRadioButton(self.groupBox)
        self.vRBf_7.setObjectName("vRBf_7")
        self.verticalLayout.addWidget(self.vRBf_7)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.vRBs_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.vRBs_1.setObjectName("vRBs_1")
        self.verticalLayout_2.addWidget(self.vRBs_1)

        self.vRBs_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.vRBs_2.setObjectName("vRBs_2")
        self.verticalLayout_2.addWidget(self.vRBs_2)

        self.vRBs_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.vRBs_3.setObjectName("vRBs_3")
        self.verticalLayout_2.addWidget(self.vRBs_3)

        self.vRBs_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.vRBs_4.setObjectName("vRBs_4")
        self.verticalLayout_2.addWidget(self.vRBs_4)

        self.vRBs_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.vRBs_5.setObjectName("vRBs_5")
        self.verticalLayout_2.addWidget(self.vRBs_5)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.vRBt_1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.vRBt_1.setObjectName("vRBt_1")
        self.verticalLayout_3.addWidget(self.vRBt_1)

        self.vRBt_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.vRBt_2.setObjectName("vRBt_2")
        self.verticalLayout_3.addWidget(self.vRBt_2)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        TabWidget.addTab(self.tab, "")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.aRBf_1 = QtWidgets.QRadioButton(self.tab1)
        self.aRBf_1.setObjectName("aRBf_1")
        self.horizontalLayout_3.addWidget(self.aRBf_1)

        self.spinBox = QtWidgets.QSpinBox(self.tab1)
        self.spinBox.setEnabled(False)
        self.spinBox.setMinimum(-99)
        self.spinBox.setProperty("value", -1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.aRBf_2 = QtWidgets.QRadioButton(self.tab1)
        self.aRBf_2.setChecked(True)
        self.aRBf_2.setObjectName("aRBf_2")
        self.verticalLayout_5.addWidget(self.aRBf_2)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Settings"))
        self.groupBox.setTitle(_translate("TabWidget", "Полный кадр"))
        self.vRBf_1.setText(_translate("TabWidget", "GrayScale"))
        self.vRBf_2.setText(_translate("TabWidget", "Negative"))
        self.vRBf_3.setText(_translate("TabWidget", "Sepia"))
        self.vRBf_4.setText(_translate("TabWidget", "Blue Sepia"))
        self.vRBf_5.setText(_translate("TabWidget", "Gradient"))
        self.vRBf_6.setText(_translate("TabWidget", "Noise"))
        self.vRBf_7.setText(_translate("TabWidget", "None"))  # <---
        self.vRBf_7.setChecked(True)

        self.groupBox_2.setTitle(_translate("TabWidget", "Части кадра"))
        self.vRBs_1.setText(_translate("TabWidget", "Контуры в кадре"))
        self.vRBs_2.setText(_translate("TabWidget", "Поиск людей"))
        self.vRBs_3.setText(_translate("TabWidget", "Силуэт тренера"))
        self.vRBs_3.setEnabled(False)
        self.vRBs_4.setText(_translate("TabWidget", "Контур тренера"))
        self.vRBs_5.setText(_translate("TabWidget", "None"))
        self.vRBs_5.setChecked(True)

        self.groupBox_3.setTitle(_translate("TabWidget", "Остальное"))
        self.vRBt_1.setText(_translate("TabWidget", "Deep Dream"))
        self.vRBt_1.setEnabled(False)
        self.vRBt_2.setText(_translate("TabWidget", "Waking Life"))
        self.vRBt_2.setEnabled(False)

        self.label_2.setText(_translate("TabWidget", "Start:"))
        self.label_3.setText(_translate("TabWidget", "End:"))
        self.pushButton.setText(_translate("TabWidget", "Confirm and cancel"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Video"))

        self.aRBf_1.setText(_translate("TabWidget", "Искажение"))
        self.aRBf_2.setText(_translate("TabWidget", "None"))
        self.pushButton_2.setText(_translate("TabWidget", "Confirm and cancel"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Audio"))

