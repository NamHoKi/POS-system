# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lacuc\Desktop\3\3-2\소공\폴더\payment_giftcard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Set_payment_info import Set_payment_info
from Common_function import Common_function
from Stock_management import Stock_management
from Payment_manage import Payment_manage

from datetime import datetime

class Giftcard_payment(object):
    def setupUi(self, Dialog, list_buf):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(1050, 550)
        
        self.common_function = Common_function()
        self.set_payment_info = Set_payment_info()
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.__num_buf = ''
        self.__list_buf = list_buf
        self.__check = False
        #배경 라벨
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1071, 681))
        self.label.setStyleSheet("background-image: url(image/mh3.PNG);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        #카드 번호 입력칸
        self.gift_num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.gift_num1.setGeometry(QtCore.QRect(83, 312, 125, 61))
        self.gift_num1.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/1313.png);\n"
                                     "font: 28pt \"Arial\";")
        self.gift_num1.setObjectName("gift_num1")

        self.gift_num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.gift_num2.setGeometry(QtCore.QRect(209, 312, 125, 61))
        self.gift_num2.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/1313.png);\n"
                                     "font: 28pt \"Arial\";")
        self.gift_num2.setObjectName("gift_num2")

        self.gift_num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.gift_num3.setGeometry(QtCore.QRect(335, 312, 125, 61))
        self.gift_num3.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/1313.png);\n"
                                     "font: 28pt \"Arial\";")
        self.gift_num3.setObjectName("gift_num3")

        self.gift_num4 = QtWidgets.QLineEdit(self.centralwidget)
        self.gift_num4.setGeometry(QtCore.QRect(464, 312, 125, 61))
        self.gift_num4.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/1313.png);\n"
                                     "font: 28pt \"Arial\";")
        self.gift_num4.setObjectName("gift_num4")

        #숫자 버튼들
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(615, 150, 130, 93))
        self.b7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.b7_clicked)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(615, 245, 130, 93))
        self.b4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.b4_clicked)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(616, 338, 130, 93))
        self.b1.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1_clicked)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(880, 338, 130, 93))
        self.b3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3_clicked)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(880, 245, 130, 93))
        self.b6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.b6_clicked)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(881, 150, 130, 93))
        self.b9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.b9_clicked)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(750, 150, 130, 93))
        self.b8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.b8_clicked)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(749, 245, 130, 93))
        self.b5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.b5_clicked)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(750, 338, 130, 93))
        self.b2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2_clicked)
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(750, 432, 130, 93))
        self.b0.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b0.setText("")
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(self.b0_clicked)
        #지우기 버튼
        self.b_erase = QtWidgets.QPushButton(self.centralwidget)
        self.b_erase.setGeometry(QtCore.QRect(615, 432, 130, 93))
        self.b_erase.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b_erase.setText("")
        self.b_erase.setObjectName("b_erase")
        self.b_erase.clicked.connect(self.b_erase_clicked)
        #완료 버튼
        self.b_ok = QtWidgets.QPushButton(self.centralwidget)
        self.b_ok.setGeometry(QtCore.QRect(881, 432, 130, 93))
        self.b_ok.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b_ok.setText("")
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.b_ok_cilcked)


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
        n = len(self.__num_buf)
        t = int(n / 5)

        if t == 0:
            self.gift_num1.setText(self.__num_buf[:n])
        elif t == 1:
            self.gift_num1.setText(self.__num_buf[:5])
            self.gift_num2.setText(self.__num_buf[5:n])
        elif t == 2:
            self.gift_num1.setText(self.__num_buf[:5])
            self.gift_num2.setText(self.__num_buf[5:10])
            self.gift_num3.setText(self.__num_buf[10:n])
        elif t == 3:
            self.gift_num1.setText(self.__num_buf[:5])
            self.gift_num2.setText(self.__num_buf[5:10])
            self.gift_num3.setText(self.__num_buf[10:15])
            self.gift_num4.setText(self.__num_buf[15:n])
        else:
            self.gift_num1.setText(self.__num_buf[:5])
            self.gift_num2.setText(self.__num_buf[5:10])
            self.gift_num3.setText(self.__num_buf[10:15])
            self.gift_num4.setText(self.__num_buf[15:20])
            self.__num_buf = self.__num_buf[:20]

    def b_erase_clicked(self):
        '''
        초기화면으로 리셋함
        :return:
        '''
        self.__num_buf = ''
        self.gift_num1.setText("")
        self.gift_num2.setText("")
        self.gift_num3.setText("")
        self.gift_num4.setText("")

    def __result_print(self):
        total_money, discount, result, get_money, rest_money = 0, 0, 0, 0, 0

        index = 0
        for i in self.__list_buf:
            total_money += int(i[4])
            discount += self.common_function.event_processing(self.__list_buf,index)
            result = total_money - discount
            index += 1

        return result

    def b_ok_cilcked(self):
        '''
        상품권번호를 확인하고 조건에 만족하면 결제 내역을 저장하고 영수증 출력
        :return:
        '''
        if not self.common_function.check_number(self.__num_buf):
            return
        if len(self.__num_buf) == 20:
            check = False
            with open('text/card_check.txt','r',encoding='utf-8') as f:
                if f is not None:
                    buf = f.read()
                    check = True

            with open('text/giftcard_check.txt','w',encoding='utf-8') as f:
                if  check and buf != '':
                    buf = int(buf) + 1
                    f.write(str(buf))
                else:
                    f.write('1')
            payment_number = self.set_payment_info.set_payment_number()
            now = self.set_payment_info.read_datetime()
            method = '상품권'
            method_info = str(self.__num_buf)
            temp = self.common_function.result_print(self.__list_buf)
            total_price = self.common_function.result_print(self.__list_buf)[2]
            self.set_payment_info.send_payment_result(payment_number, now, method, method_info, total_price)

            self.__list_buf = self.common_function.modify_list_buf(self.__list_buf)
            self.set_payment_info.send_payment_detail(self.__list_buf, payment_number)

            stock_manager = Stock_management()
            for i in self.__list_buf:
                pro = stock_manager.product_search(i[0])
                quan = pro[2]
                stock_manager.product_quan_modification(i[0], quan - int(i[3]))

            self.common_function.msg_box('결제가 완료되었습니다.     ')
            self.__check = True

            # 영수증 출력
            pay = Payment_manage()
            last_receipt_number = int(self.set_payment_info.set_payment_number()) - 1
            detail = pay.return_detail(str(last_receipt_number))
            now = datetime.now()
            date = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(
                now.minute) + ':' + str(now.second)
            self.common_function.receipt_print_form(date, detail,last_receipt_number)
        else:
            self.common_function.msg_box('유효하지 않는 상품권번호입니다.    ')


