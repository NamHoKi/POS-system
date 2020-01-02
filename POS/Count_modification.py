# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\count_modification.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from Common_function import Common_function

class Count_modification(QDialog):
    def setupUi(self,Dialog,main_mode):
        import count_modification_rc
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(890, 439)
        
        self.common_function = Common_function()
        self.__check = False
        self.__target = True #숫자 버튼을 쓸 곳 구분을 위함 // Ture : 번호 칸 , False : 수량 칸

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        #배경 라벨
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(2, 0, 888, 440))
        self.bg.setStyleSheet("border-image: url(:/newPrefix/cntmodification.png);")
        self.bg.setPixmap(QtGui.QPixmap(":/image/image/cntmodification.png"))
        self.bg.setObjectName("bg")
        #완료 버튼
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(730, 320, 126, 85))
        self.ok.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.ok_clicked)
        #지우기 버튼
        self.my_del = QtWidgets.QPushButton(self.centralwidget)
        self.my_del.setGeometry(QtCore.QRect(467, 320, 126, 85))
        self.my_del.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.my_del.setObjectName("my_del")
        self.my_del.clicked.connect(self.my_del_clicked)
        #번호 버튼
        self.num = QtWidgets.QPushButton(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(330, 140, 111, 61))
        self.num.setStyleSheet("border-image: url(:/newPrefix/4.png);\n"
"font: 24pt \"Arial\";")
        self.num.setObjectName("num")
        self.num.setText("")
        self.num.clicked.connect(self.num_clicked)
        #수량 버튼
        self.cnt = QtWidgets.QPushButton(self.centralwidget)
        self.cnt.setGeometry(QtCore.QRect(330, 240, 111, 61))
        self.cnt.setStyleSheet("border-image: url(:/newPrefix/4.png);\n"
"font: 24pt \"Arial\";")
        self.cnt.setObjectName("cnt")
        self.cnt.setText("")
        self.cnt.clicked.connect(self.cnt_clicked)
        #숫자 버튼들
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(467, 131, 126, 85))
        self.b4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.b4_clicked)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(730, 37, 126, 85))
        self.b9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.b9_clicked)
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(599, 320, 126, 85))
        self.b0.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(self.b0_clicked)
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(467, 37, 126, 85))
        self.b7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.b7_clicked)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(599, 225, 126, 85))
        self.b2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2_clicked)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(467, 225, 126, 85))
        self.b1.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1_clicked)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(599, 131, 126, 85))
        self.b5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.b5_clicked)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(730, 131, 126, 85))
        self.b6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.b6_clicked)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(730, 225, 126, 85))
        self.b3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3_clicked)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(599, 37, 126, 85))
        self.b8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.b8_clicked)

    def ok_clicked(self):
        '''
        빈칸 유무 체크 후, 파일에 번호와 수량을 기록함
        :return:
        '''
        if self.num.text() == '' or self.cnt.text() == '':
            self.common_function.msg_box('빈칸이 있습니다 !     ')
        else:
            num = self.num.text()
            cnt = self.cnt.text()
            text = num+' ' + cnt
            with open('text/count_modification_buf.txt','w',encoding='utf-8') as f:
                f.write(text)
            self.common_function.msg_box('입력되었습니다.\n창을 닫으십시오.   ')
            self.__check = True

    def my_del_clicked(self):
        '''
        self.__target 에 따라 번호 칸이나 수량 칸을 지움
        :return:
        '''
        if self.__target:
            self.num.setText("")
        else:
            self.cnt.setText("")

    def num_clicked(self):
        '''
        번호 버튼 클릭 이벤트
        버튼들의 타겟을 번호 칸으로 변경함
        :return:
        '''
        self.__target = True

    def cnt_clicked(self):
        '''
        수량 버튼 클릭 이벤트
        버튼들의 타겟을 수량 칸으로 변경함
        :return:
        '''
        self.__target = False

    def b0_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "0")
        else:
            self.cnt.setText(self.cnt.text() + "0")

    def b1_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "1")
        else:
            self.cnt.setText(self.cnt.text() + "1")

    def b2_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "2")
        else:
            self.cnt.setText(self.cnt.text() + "2")

    def b3_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "3")
        else:
            self.cnt.setText(self.cnt.text() + "3")

    def b4_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "4")
        else:
            self.cnt.setText(self.cnt.text() + "4")

    def b5_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "5")
        else:
            self.cnt.setText(self.cnt.text() + "5")

    def b6_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "6")
        else:
            self.cnt.setText(self.cnt.text() + "6")

    def b7_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "7")
        else:
            self.cnt.setText(self.cnt.text() + "7")

    def b8_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "8")
        else:
            self.cnt.setText(self.cnt.text() + "8")

    def b9_clicked(self):
        '''
        self.__target에 따라 숫자를 입력함
        :return:
        '''
        if self.__target:
            self.num.setText(self.num.text() + "9")
        else:
            self.cnt.setText(self.cnt.text() + "9")