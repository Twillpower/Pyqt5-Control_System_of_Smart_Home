from ui.Control_System_of_Smart_Home import Ui_MainWindow as A_Ui
from ui.main_interface import Ui_MainWindow as B_Ui
from ui.LED import Ui_LED as LED
from ui.空调设置 import Ui_MainWindow as kt_Ui
from ui.窗帘设置 import Ui_MainWindow as cl_Ui
from usart import usart

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel
import sys


class login_Ui(QtWidgets.QMainWindow, A_Ui):
    def __init__(self):
        super(login_Ui, self).__init__()
        self.setupUi(self)


class Main_Ui(QtWidgets.QMainWindow, B_Ui):
    def __init__(self):
        super(Main_Ui, self).__init__()
        self.setupUi(self)


class LED_UI(QtWidgets.QMainWindow, LED):
    def __init__(self):
        super(LED_UI, self).__init__()
        self.setupUi(self)


class kt_UI(QtWidgets.QMainWindow, kt_Ui):
    def __init__(self):
        super(kt_UI, self).__init__()
        self.setupUi(self)


class cl_UI(QtWidgets.QMainWindow, cl_Ui):
    def __init__(self):
        super(cl_UI, self).__init__()
        self.setupUi(self)


class Update(QThread):
    uart = usart.usart()
    update_led = pyqtSignal(str)  # 信号类
    update_kt = pyqtSignal(str)
    update_cl = pyqtSignal(str)

    def run(self):
        while True:
            self.uart.read_data()
            led_date = self.uart.str1[0][2:]
            kt_date = self.uart.str1[1][:]
            cl_date = self.uart.str1[0][2:]
            self.update_led.emit(str(led_date))  # 发送信号
            self.update_kt.emit(str(kt_date))
            self.update_cl.emit(str(cl_date))


class Controller:
    def __init__(self):
        self.led_state = 2
        self.kt_state = 1
        self.cl_state = 1
        self.login = login_Ui()
        self.MainWin = Main_Ui()
        self.led = LED_UI()
        self.kt = kt_UI()
        self.cl = cl_UI()

    # 登陆界面
    def show_login(self):
        self.login.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.login.pushButton.clicked.connect(self.show_main)
        self.login.show()

    # 主界面
    def show_main(self):
        user = self.login.lineEdit.text()
        password = self.login.lineEdit_2.text()
        # print("账号：",user, "密码",password)

        if (user == "123" and password == "456"):
            self.MainWin.pushButton.clicked.connect(self.Show_setled)
            self.MainWin.pushButton_2.clicked.connect(self.Show_setkt)
            self.MainWin.pushButton_3.clicked.connect(self.Show_setcl)

            self.backend = Update()
            self.backend.update_led.connect(self.ledDisplay)  # 将线程与控件绑定
            self.backend.update_kt.connect(self.ktDisplay)
            self.backend.update_cl.connect(self.clDisplay)
            self.backend.start()  # 开始线程

            self.MainWin.show()
            # self.login.close()

    def ledDisplay(self, data):
        self.MainWin.label_5.setText(data)
        self.led.label_5.setText(data)

    def ktDisplay(self, data):
        self.MainWin.label_16.setText(data)
        self.kt.label_4.setText(data)

    def clDisplay(self, data):
        self.MainWin.label_20.setText(data)
        self.cl.label_3.setText(data)

    # LED
    def Show_setled(self):
        self.led.timeEdit.timeChanged.connect(self.LED_onTimeChanged)
        self.led.timeEdit_2.timeChanged.connect(self.LED_onTimeChanged)
        self.led.pushButton.clicked.connect(self.LED_state)
        self.led.show()

    def LED_onTimeChanged(self):
        dateTime_1 = self.led.timeEdit.dateTime()
        dateTime_2 = self.led.timeEdit_2.dateTime()
        self.LEDdateTime = dateTime_1.toString('hh:mm') + dateTime_2.toString('/hh:mm')
        self.led.label_31.setText(self.LEDdateTime)
        self.MainWin.label_31.setText(self.LEDdateTime)

    def LED_state(self):
        if (self.led_state == 1):
            self.led.label_4.setText("开")
            self.MainWin.label_4.setText("开")
            self.led_state = 2
        elif (self.led_state == 2):
            self.led.label_4.setText("关")
            self.MainWin.label_4.setText("关")
            self.led_state = 1

    # 空调
    def Show_setkt(self):
        self.kt.timeEdit.timeChanged.connect(self.KT_onTimeChanged)
        self.kt.timeEdit_2.timeChanged.connect(self.KT_onTimeChanged)
        self.kt.pushButton.clicked.connect(self.KT_state)
        self.kt.doubleSpinBox.valueChanged.connect(self.set_temp)
        self.kt.show()

    def KT_onTimeChanged(self):
        dateTime_1 = self.kt.timeEdit.dateTime()
        dateTime_2 = self.kt.timeEdit_2.dateTime()
        self.LEDdateTime = dateTime_1.toString('hh:mm') + dateTime_2.toString('/hh:mm')
        self.kt.label_32.setText(self.LEDdateTime)
        self.MainWin.label_32.setText(self.LEDdateTime)

    def KT_state(self):
        if (self.kt_state == 1):
            self.kt.label_11.setText("开")
            self.MainWin.label_11.setText("开")
            self.kt_state = 2
        elif (self.kt_state == 2):
            self.kt.label_11.setText("关")
            self.MainWin.label_11.setText("关")
            self.kt_state = 1

    def set_temp(self):
        self.kt.label_12.setText(self.kt.doubleSpinBox.text())
        self.MainWin.label_12.setText(self.kt.doubleSpinBox.text())

    # 窗帘
    def Show_setcl(self):
        self.cl.timeEdit.timeChanged.connect(self.CL_onTimeChanged)
        self.cl.timeEdit_2.timeChanged.connect(self.CL_onTimeChanged)
        self.cl.pushButton.clicked.connect(self.CL_state)
        self.cl.show()

    def CL_onTimeChanged(self):
        dateTime_1 = self.cl.timeEdit.dateTime()
        dateTime_2 = self.cl.timeEdit_2.dateTime()
        self.LEDdateTime = dateTime_1.toString('hh:mm') + dateTime_2.toString('/hh:mm')
        self.cl.label_27.setText(self.LEDdateTime)
        self.MainWin.label_27.setText(self.LEDdateTime)

    def CL_state(self):
        if (self.cl_state == 1):
            self.cl.label_24.setText("开")
            self.MainWin.label_24.setText("开")
            self.cl_state = 2
        elif (self.cl_state == 2):
            self.cl.label_24.setText("关")
            self.MainWin.label_24.setText("关")
            self.cl_state = 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
