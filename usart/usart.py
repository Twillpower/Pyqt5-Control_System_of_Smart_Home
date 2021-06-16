import serial

class usart():
    def __init__(self):
        self.ser = serial.Serial( #下面这些参数根据情况修改
            port='COM5',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.data = ''

    def read_data(self):
        self.data = self.ser.readline()
        self.str1 = str(self.data).split(" ")
        print(self.str1)
        print(self.str1[0][2:], self.str1[1][:], self.str1[2][:-3])

if __name__=="__main__":
    uart = usart()