# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '空调设置.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 30, 821, 431))
        self.frame_3.setStyleSheet("#frame_3{background-color: rgb(24, 211, 83);}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(310, 0, 511, 431))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 150, 311, 131))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(0, 0, 251, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/image/空调.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(260, 60, 72, 15))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(840, 390, 151, 55))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(19, 0, 0)))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_3.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 0, 0)))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_3.addWidget(self.timeEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 70, 92, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 320, 92, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 490, 112, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(410, 490, 112, 19))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(840, 240, 70, 22))
        self.doubleSpinBox.setMinimum(10.0)
        self.doubleSpinBox.setMaximum(40.0)
        self.doubleSpinBox.setProperty("value", 22.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "空调设置"))
        self.label_7.setText(_translate("MainWindow", "状态"))
        self.label_8.setText(_translate("MainWindow", "温度(℃)"))
        self.label_13.setText(_translate("MainWindow", "耗能(kwh)"))
        self.label_28.setText(_translate("MainWindow", "阈值(time:morning/night)"))
        self.label_11.setText(_translate("MainWindow", "关"))
        self.label_12.setText(_translate("MainWindow", "22"))
        self.label_14.setText(_translate("MainWindow", "76"))
        self.label_32.setText(_translate("MainWindow", "19:00/23:00"))
        self.label_3.setText(_translate("MainWindow", "当前温度(℃)"))
        self.label_4.setText(_translate("MainWindow", "22"))
        self.label_9.setText(_translate("MainWindow", "空调"))
        self.label_10.setText(_translate("MainWindow", "night:"))
        self.label_2.setText(_translate("MainWindow", "morning:"))
        self.pushButton.setText(_translate("MainWindow", "开/关"))
        self.pushButton_2.setText(_translate("MainWindow", "清零"))
        self.radioButton_2.setText(_translate("MainWindow", "自动"))
        self.radioButton.setText(_translate("MainWindow", "手动"))
import main_interface_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
