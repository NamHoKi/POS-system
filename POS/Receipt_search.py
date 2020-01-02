# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\receipt_search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Payment_manage import Payment_manage
from datetime import datetime as dt
from Common_function import Common_function

class Receipt_search(object):
    def setupUi(self, Dialog):
        import yj_rc

        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(889, 497)
        
        self.common_function = Common_function()
        self.__check = False
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        #배경 라벨
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 887, 476))
        self.label.setStyleSheet("border-image: url(:/newPrefix/receiptsearch.png);")
        self.label.setPixmap(QtGui.QPixmap("image/receiptsearch.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        #영수증 바코드 입력 칸
        self.reciept_barcode = QtWidgets.QLineEdit(self.centralwidget)
        self.reciept_barcode.setGeometry(QtCore.QRect(323, 213, 471, 89))
        self.reciept_barcode.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                           "font: 28pt \"Arial\";\n"
                                           "border-image: url(:/newPrefix/fr8.png);")
        self.reciept_barcode.setObjectName("reciept_barcode")

        self.reciept_del = QtWidgets.QPushButton(self.centralwidget)
        self.reciept_del.setGeometry(QtCore.QRect(200, 340, 151, 101))
        self.reciept_del.setStyleSheet("border-image: url(:/newPrefix/yj_del.png);")
        self.reciept_del.setObjectName("reciept_del")

        self.reciept_ok = QtWidgets.QPushButton(self.centralwidget)
        self.reciept_ok.setGeometry(QtCore.QRect(540, 340, 151, 101))
        self.reciept_ok.setStyleSheet("border-image: url(:/newPrefix/yj_complt.png);")
        self.reciept_ok.setObjectName("reciept_ok")
        self.reciept_ok.clicked.connect(self.reciept_ok_clicked)

    def reciept_ok_clicked(self):
        '''
        '완료' 버튼 클릭 이벤트
        유효한 바코드인지 아닌지 확인 후, 유효하다면 조회 하고 파일에 기록함
        :return:
        '''
        pay = Payment_manage()
        receipt_num = self.reciept_barcode.text()

        paylist = pay.check_payment_number(receipt_num)
        if paylist is None or len(paylist) == 0 or paylist[0] == '':
            self.common_function.msg_box('유효하지 않은 영수증 바코드입니다.     ')
            return

        for i in range(len(paylist)):
            paylist[i][1] = dt.strftime(paylist[i][1], '%Y-%m-%d %H:%M:%S')

        buf = ''
        check = False
        text = self.common_function.text_read('text/receipt_search_buf.txt')
        if text != '':
            check = True
            text = text.split('\n')
            check_num = str(text[0])
        if check is False:
            check_num = '1'
            buf += check_num + '\n'
        else:
            buf += str(int(check_num) + 1) + '\n'
        paylist = paylist[0]
        for token in paylist:
            buf += str(token) + '#'
        self.common_function.text_write('text/receipt_search_buf.txt',buf)
        self.common_function.msg_box('조회됐습니다.\n창을 닫으십시오.     ')
        self.__check = True

    def reciept_del_clicked(self):
        '''
        '지우기'버튼 클릭 이벤트
        영수증 바코드 칸을 초기화 함
        :return:
        '''
        self.reciept_barcode.setText("")
