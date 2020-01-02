# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lacuc\Desktop\SaleCheck.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Payment_manage import Payment_manage
from PyQt5.QtGui import QIcon
from Common_function import Common_function
from List_print_function import List_print_function

class Sales_check(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(1400, 726)

        self.list_print_function = List_print_function()
        self.common_function = Common_function()
        self.__year = None
        self.__month = None
        self.__day = None
        self.__mode = None

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        #배경 라벨
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1400, 726))
        self.label.setPixmap(QtGui.QPixmap("image/whitesales.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        #달력 위젯
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(23, 23, 951, 411))
        self.calendar.setGridVisible(False)
        self.calendar.setObjectName("calendar")
        #일별 매출 버튼
        self.bday = QtWidgets.QPushButton(self.centralwidget)
        self.bday.setGeometry(QtCore.QRect(1001, 389, 122, 121))
        self.bday.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.bday.setObjectName("bday")
        #월별 매출 버튼
        self.bmonth = QtWidgets.QPushButton(self.centralwidget)
        self.bmonth.setGeometry(QtCore.QRect(1129, 389, 122, 121))
        self.bmonth.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.bmonth.setObjectName("bmonth")
        #연별 매출 버튼
        self.byear = QtWidgets.QPushButton(self.centralwidget)
        self.byear.setGeometry(QtCore.QRect(1258, 389, 121, 121))
        self.byear.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.byear.setObjectName("byear")

        # 결제 수단별 매출 버튼
        self.bsalemethod = QtWidgets.QPushButton(self.centralwidget)
        self.bsalemethod.setGeometry(QtCore.QRect(1001, 516, 185, 121))
        self.bsalemethod.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.bsalemethod.setObjectName("bsalemethod")

        # 제품별 매출 버튼
        self.bsalegoods = QtWidgets.QPushButton(self.centralwidget)
        self.bsalegoods.setGeometry(QtCore.QRect(1193, 516, 185, 121))
        self.bsalegoods.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.bsalegoods.setObjectName("bsalegoods")
        self.bsalegoods.clicked.connect(self.bsalegoods_clicked)

        self.choosedate = QtWidgets.QLineEdit(self.centralwidget)
        self.choosedate.setGeometry(QtCore.QRect(1011, 102, 356, 75))
        self.choosedate.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                      "font: 28pt \"Arial\";"
                                      "border-image: url(image/1.png);")
        self.choosedate.setObjectName("choosedate")

        # 총 매출
        self.allsales = QtWidgets.QLineEdit(self.centralwidget)
        self.allsales.setGeometry(QtCore.QRect(1011, 240, 357, 131))
        self.allsales.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                    "font: 28pt \"Arial\";"
                                    "border-image: url(image/2.png);")
        self.allsales.setObjectName("allsales")

        # 사용종료 버튼
        self.boff = QtWidgets.QPushButton(self.centralwidget)
        self.boff.setGeometry(QtCore.QRect(1000, 643, 380, 61))
        self.boff.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.boff.setObjectName("boff")

        # 결제 수단별 이미지
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_2.setPixmap(QtGui.QPixmap("image/fr7.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.moneytxt = QtWidgets.QLineEdit(self.centralwidget)
        self.moneytxt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.moneytxt.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                    "font: 28pt \"Arial\";"
                                    "border-image: url(image/3.png);")
        self.moneytxt.setObjectName("moneytxt")

        self.cardtxt = QtWidgets.QLineEdit(self.centralwidget)
        self.cardtxt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.cardtxt.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                   "font: 28pt \"Arial\";"
                                   "border-image: url(image/3.png);")
        self.cardtxt.setObjectName("cardtxt")

        self.gifttxt = QtWidgets.QLineEdit(self.centralwidget)
        self.gifttxt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.gifttxt.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                   "font: 28pt \"Arial\";"
                                   "border-image: url(image/3.png);")
        self.gifttxt.setObjectName("gifttxt")

        # 결제수단별 리스트 출력 하는곳
        self.goodslistview = QtWidgets.QTextEdit(self.centralwidget)
        self.goodslistview.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goodslistview.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                         "font: 20pt \"Fixedsys\";"
                                         "border-image: url(image/fr6.png);")
        self.goodslistview.setObjectName("goodslistview")

        self.sales_list_attribute = QtWidgets.QPushButton(self.centralwidget)
        self.sales_list_attribute.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.sales_list_attribute.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                                "border-image: url(image/sales_list_attribute.png);")
        self.sales_list_attribute.setObjectName('sales_list_attribute')

        self.bday.clicked.connect(self.bday_clicked)
        self.bmonth.clicked.connect(self.bmonth_clicked)
        self.byear.clicked.connect(self.byear_clicked)
        self.bsalemethod.clicked.connect(self.bsalemethod_clicked)
        self.bsalegoods.clicked.connect(self.bsalegoods_clicked)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def bday_clicked(self):
        '''
        '일별 매출' 버튼 클릭 이벤트
        해당 날짜의 '년,월,일'을 받아와서 그 날의 매출을 출력함
        :return:
        '''
        self.__mode = 'day'
        date = self.calendar.selectedDate()
        tmp = date.toString("yyyy-MM-dd")
        self.__year, self.__month, self.__day = tmp.split('-')
        self.choosedate.setText("  " + self.__year + "년" + self.__month + "월" + self.__day + "일")
        pay = Payment_manage()
        total_money = pay.check_sales_today(int(self.__year), int(self.__month), int(self.__day))
        self.allsales.setText(" " + self.common_function.insert_comma(total_money) + "원")

    def bmonth_clicked(self):
        '''
        '월별 매출' 버튼 클릭 이벤트
        해당 날짜의 '년,월'을 받아와서 그 달의 매출을 출력함
        :return:
        '''
        self.__mode = 'month'
        date = self.calendar.selectedDate()
        tmp = date.toString("yyyy-MM-dd")
        self.__year, self.__month, self.__day = tmp.split('-')
        # self.__day = None
        self.choosedate.setText("  " + self.__year + "년" + self.__month + "월")
        pay = Payment_manage()
        total_money = pay.check_sales_month(int(self.__year), int(self.__month))
        self.allsales.setText(" " + self.common_function.insert_comma(total_money) + "원")

    def byear_clicked(self):
        '''
        '연별 매출' 버튼 클릭 이벤트
        해당 날짜의 '년'을 받아와서 그 해의 매출을 출력함
        :return:
        '''
        self.__mode = 'year'
        year = str(self.calendar.yearShown())
        self.__year = year
        # self.__month, self.__day = None, None
        self.choosedate.setText("  " + year + "년")
        pay = Payment_manage()
        total_money = pay.check_sales_year(int(self.__year))
        self.allsales.setText(" " + self.common_function.insert_comma(total_money) + "원")

    def bsalemethod_clicked(self):
        '''
        '결제 수단별 매출' 버튼 클릭 이벤트
        이전에 클릭한 버튼에 따라 결제 수단별 매출금액을 출력함
        :return:
        '''
        if self.__year == None and self.__month == None and self.__day == None:
            self.common_function.msg_box('날짜를 클릭하시오.     ')
            return

        self.label_2.setGeometry(QtCore.QRect(12, 449, 973, 266))

        self.moneytxt.setGeometry(QtCore.QRect(48, 592, 262, 86))

        self.cardtxt.setGeometry(QtCore.QRect(369, 592, 262, 86))

        self.gifttxt.setGeometry(QtCore.QRect(689, 592, 262, 86))

        self.goodslistview.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.sales_list_attribute.setGeometry(QtCore.QRect(0, 0, 0, 0))

        date = self.calendar.selectedDate()
        tmp = date.toString("yyyy-MM-dd")
        self.__year, self.__month, self.__day = tmp.split('-')

        cash, card, gift = 0, 0, 0
        pay = Payment_manage()

        if self.__mode == 'day':
            paylist = pay.check_sales_day_return_paylist(self.__year, self.__month, self.__day)
            if (len(paylist) == 0):
                pass
            else:
                real_paylist = sum(paylist, [])
                for i in real_paylist:
                    if i[2] == '카드':
                        card += i[4]
                    if i[2] == '현금':
                        cash += i[4]
                    if i[2] == '상품권':
                        gift += i[4]

        elif self.__mode == 'month':
            paylist = pay.check_sales_month_return_paylist(self.__year, self.__month)
            if (len(paylist) == 0):
                pass
            else:
                real_paylist = sum(paylist, [])
                for i in real_paylist:
                    if i[2] == '카드':
                        card += i[4]
                    if i[2] == '현금':
                        cash += i[4]
                    if i[2] == '상품권':
                        gift += i[4]

        elif self.__mode == 'year':
            paylist = pay.check_sales_year_return_paylist(self.__year)
            if (len(paylist) == 0):
                pass
            else:
                real_paylist = sum(paylist, [])
                for i in real_paylist:
                    if i[2] == '카드':
                        card += i[4]
                    if i[2] == '현금':
                        cash += i[4]
                    if i[2] == '상품권':
                        gift += i[4]

        self.moneytxt.setText(' ' + self.common_function.insert_comma(cash) + '원')
        self.cardtxt.setText(' ' + self.common_function.insert_comma(card) + '원')
        self.gifttxt.setText(' ' + self.common_function.insert_comma(gift) + '원')

    def bsalegoods_clicked(self):
        '''
        결제 수단별 매출' 버튼 클릭 이벤트
        이전에 클릭한 버튼에 따라 제품별 매출금액을 출력함
        :return:
        '''
        if self.__year == None and self.__month == None and self.__day == None:
            self.common_function.msg_box('날짜를 클릭하시오.     ')
            return

        date = self.calendar.selectedDate()
        tmp = date.toString("yyyy-MM-dd")
        self.__year, self.__month, self.__day = tmp.split('-')

        self.goodslistview.setGeometry(QtCore.QRect(13, 449, 973, 266))

        self.sales_list_attribute.setGeometry(QtCore.QRect(26, 455, 935, 41))

        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.moneytxt.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.cardtxt.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.gifttxt.setGeometry(QtCore.QRect(0, 0, 0, 0))

        buf = '\n\n\n\n'
        pay = Payment_manage()

        if self.__mode == 'day':
            paylist = pay.check_sales_product_real_day(int(self.__year), int(self.__month), int(self.__day))

            if (len(paylist) == 0):
                pass

            else:
                real_paylist = sum(paylist, [])
                sorted_paylist = sorted(real_paylist, key=lambda paylist: paylist[5], reverse=True)
                n = 1
                for text in sorted_paylist:  # text -> 이름 수량 원가 영수증번호 행사상품 총가격 제품번호

                    if n < 10:
                        num = '0' + str(n)
                    else:
                        num = str(n)
                    # 번호 바코드 품목명 단가 수량 금액 행사
                    buf += self.list_print(num, text[6], text[0], text[2], text[1], text[5], text[4])
                    n += 1
        elif self.__mode == 'month':
            paylist = pay.check_sales_product_real_month(int(self.__year), int(self.__month))

            if (len(paylist) == 0):
                pass

            else:
                real_paylist = sum(paylist, [])
                sorted_paylist = sorted(real_paylist, key=lambda paylist: paylist[5], reverse=True)

                n = 1
                for text in sorted_paylist:  # text -> 이름 수량 원가 영수증번호 행사상품 총가격 제품번호
                    total = self.common_function.event_processing_return(text[4], text[1], text[2])

                    if n < 10:
                        num = '0' + str(n)
                    else:
                        num = str(n)
                    # 번호 바코드 품목명 단가 수량 금액 행사
                    buf += self.list_print(num, text[6], text[0], text[2], text[1], text[5], text[4])
                    n += 1
        elif self.__mode == 'year':
            paylist = pay.check_sales_product_real_year(int(self.__year))

            if (len(paylist) == 0):
                pass

            else:
                real_paylist = sum(paylist, [])
                sorted_paylist = sorted(real_paylist, key=lambda paylist: paylist[5], reverse=True)

                n = 1
                for text in sorted_paylist:  # text -> 이름 수량 원가 영수증번호 행사상품 총가격 제품번호
                    total = self.common_function.event_processing_return(text[4], text[1], text[2])

                    if n < 10:
                        num = '0' + str(n)
                    else:
                        num = str(n)
                    # 번호 바코드 품목명 단가 수량 금액 행사
                    buf += self.list_print(num,text[6],text[0],text[2],text[1],text[5],text[4])
                    n += 1

        self.goodslistview.setText(buf)

    def list_print(self,num,barcode,name,price,quantity,total_price,event):
        buf = ' ' * 4 + self.list_print_function.number_print(num) + str(barcode) + ' ' * 10 + self.list_print_function.name_print(
            name) + ' ' + self.list_print_function.price_print(price) + ' ' + self.list_print_function.count_print(
            quantity) + ' ' + self.list_print_function.price_print(str(total_price)) + '  ' + self.list_print_function.event_print(event) + '\n'
        return buf