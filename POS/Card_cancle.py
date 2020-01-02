# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\card_cancle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Common_function import Common_function
from PyQt5.QtWidgets import *

class Card_cancle(QDialog):
    def setupUi(self, Dialog):
        import pay_rc
        #Window 설정
        Dialog.setObjectName("Dialog")
        Dialog.resize(1003, 633)

        self.__num_buf = '' #카드 번호 버퍼
        self.common_function = Common_function()
        self.__check = False
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        #배경 라벨
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(1, -10, 1011, 651))
        self.bg.setStyleSheet("border-image: url(image/mh2.PNG);")
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")

        # 카드 번호 입력 칸
        self.card_num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.card_num1.setGeometry(QtCore.QRect(78, 290, 121, 61))
        self.card_num1.setStyleSheet("border-image: url(:/newPrefix/car_num.png);\n"
                                     "font: 28pt \"Arial\";")
        self.card_num1.setObjectName("card_num1")

        self.card_num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.card_num2.setGeometry(QtCore.QRect(198, 290, 121, 61))
        self.card_num2.setStyleSheet("border-image: url(:/newPrefix/car_num.png);\n"
                                     "font: 28pt \"Arial\";")
        self.card_num2.setObjectName("card_num2")

        self.card_num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.card_num3.setGeometry(QtCore.QRect(320, 290, 121, 61))
        self.card_num3.setStyleSheet("border-image: url(:/newPrefix/car_num.png);\n"
                                     "font: 28pt \"Arial\";")
        self.card_num3.setObjectName("card_num3")

        self.card_num4 = QtWidgets.QLineEdit(self.centralwidget)
        self.card_num4.setGeometry(QtCore.QRect(442, 290, 121, 61))
        self.card_num4.setStyleSheet("border-image: url(:/newPrefix/car_num.png);\n"
                                     "font: 28pt \"Arial\";")
        self.card_num4.setObjectName("card_num4")

        # 숫자 버튼
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(592, 143, 111, 81))
        self.b7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.b7_clicked)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(716, 141, 121, 81))
        self.b8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.b8_clicked)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(843, 143, 121, 81))
        self.b9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.b9_clicked)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(590, 230, 121, 81))
        self.b4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.b4_clicked)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(590, 316, 121, 81))
        self.b1.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1_clicked)
        self.b_del = QtWidgets.QPushButton(self.centralwidget)
        self.b_del.setGeometry(QtCore.QRect(588, 405, 121, 81))
        self.b_del.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b_del.setObjectName("b_del")
        self.b_del.clicked.connect(self.b_del_clicked)
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(717, 405, 121, 81))
        self.b0.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(self.b0_clicked)
        self.b_com = QtWidgets.QPushButton(self.centralwidget)
        self.b_com.setGeometry(QtCore.QRect(844, 405, 121, 81))
        self.b_com.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b_com.setObjectName("b_com")
        self.b_com.clicked.connect(self.b_com_clicked)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(718, 317, 121, 81))
        self.b2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2_clicked)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(717, 230, 121, 81))
        self.b5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.b5_clicked)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(843, 230, 121, 81))
        self.b6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.b6_clicked)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(843, 318, 121, 81))
        self.b3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3_clicked)

    def b0_clicked(self):
        self.__num_buf += '0'
        self.__write_num()

    def b1_clicked(self):
        self.__num_buf += '1'
        self.__write_num()

    def b2_clicked(self):
        self.__num_buf += '2'
        self.__write_num()

    def b3_clicked(self):
        self.__num_buf += '3'
        self.__write_num()

    def b4_clicked(self):
        self.__num_buf += '4'
        self.__write_num()

    def b5_clicked(self):
        self.__num_buf += '5'
        self.__write_num()

    def b6_clicked(self):
        self.__num_buf += '6'
        self.__write_num()

    def b7_clicked(self):
        self.__num_buf += '7'
        self.__write_num()

    def b8_clicked(self):
        self.__num_buf += '8'
        self.__write_num()

    def b9_clicked(self):
        self.__num_buf += '9'
        self.__write_num()

    def __write_num(self):
        '''
        self.__num_buf의 숫자를 각 칸에 맞게 입력시킴
        :return:
        '''
        n = len(self.__num_buf)
        t = int(n / 4)

        if t == 0:
            self.card_num1.setText(self.__num_buf[:n])
        elif t == 1:
            self.card_num1.setText(self.__num_buf[:4])
            self.card_num2.setText(self.__num_buf[4:n])
        elif t == 2:
            self.card_num1.setText(self.__num_buf[:4])
            self.card_num2.setText(self.__num_buf[4:8])
            self.card_num3.setText(self.__num_buf[8:n])
        elif t == 3:
            self.card_num1.setText(self.__num_buf[:4])
            self.card_num2.setText(self.__num_buf[4:8])
            self.card_num3.setText(self.__num_buf[8:12])
            self.card_num4.setText(self.__num_buf[12:n])
        else:
            self.card_num1.setText(self.__num_buf[:4])
            self.card_num2.setText(self.__num_buf[4:8])
            self.card_num3.setText(self.__num_buf[8:12])
            self.card_num4.setText(self.__num_buf[12:16])
            self.__num_buf = self.__num_buf[:16]

    def b_del_clicked(self):
        '''
        입력된 카드번호를 초기화함
        :return:
        '''
        self.__num_buf = ''
        self.card_num1.setText("")
        self.card_num2.setText("")
        self.card_num3.setText("")
        self.card_num4.setText("")

    def b_com_clicked(self):
        '''
        16자리가 입력되면 MainWindow로 넘겨주기 위해서 .txt 파일로 기록함
        :return:
        '''
        if self.__check:
            self.common_function.msg_box('이미 완료 되었습니다.\n창을 닫으십시오.     ')
            return
        if len(self.__num_buf) != 16:
            self.common_function.msg_box('입력이 올바르지 않습니다.     ')
            return
        if not self.common_function.check_number(self.__num_buf):
            return

        text = self.common_function.text_read('text/card_cancle.txt')
        if text == '':
            buf = '1\n'
        else:
            text = text.split('\n')
            buf = str(int(text[0]) + 1) + '\n'
        buf += self.__num_buf
        self.common_function.text_write('text/card_cancle.txt',buf)
        self.common_function.msg_box('입력되었습니다.\n창을 닫으십시오.     ')
        self.__check = True