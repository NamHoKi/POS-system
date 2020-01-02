# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

from datetime import datetime
import winsound

from Count_modification import Count_modification
from Stock_management import Stock_management
from Card_payment import Card_payment
from Goods_input import Goods_input
from Goods_modification import Goods_modification
from Giftcard_payment import Giftcard_payment
from Sales_check import Sales_check
from Receipt_search import Receipt_search
from Payment_manage import Payment_manage
from Card_cancle import Card_cancle
from Common_function import Common_function
from List_print_function import List_print_function
from Set_payment_info import Set_payment_info

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__list_buf = [] # self.list (상품 리스트 라벨)에 출력 될 리스트
        self.__mode = 'main' # 'main' or 'admin' or 'pay'
        self.__target_barcode = True # Ture : mode가 main일때, 계산 목록 // False : mode가 admin 일때, 재고 목록
        self.__receipt_buf = None # 영수증 번호 버퍼
        self.__event_print_check = False # 행사상품을 출력한 상태인지 아닌지 // 수량변경 버튼은 경우에 따라 나뉘기 때문
        self.__change_check = False # 경우를 나누기 위한 변수
        self.__staff_mode_check = True # 경우를 나누기 위한 변수
        self.__last_product = None # 결제 후, 마지막으로 계산된 결과로 영수증을 출력함

        # 자주 쓰이는 클래스 // 매번 생성하는 것보단 미리 생성
        self.common_function = Common_function()
        self.list_print_function = List_print_function()
        self.stock_manager = Stock_management()
        self.payment_manager = Payment_manage()
        self.set_payment_info = Set_payment_info()
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        #MainWindow 설정
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(1400, 726)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(True)

        # 배경 이미지 라벨
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 1, 1400, 726))
        self.bg.setPixmap(QtGui.QPixmap("image/back_ground.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")

        # 우측 중간 숫자 버튼
        self.b7 = QtWidgets.QPushButton(Dialog)
        self.b7.setGeometry(QtCore.QRect(1001, 255, 90, 60))
        self.b7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.b7_clicked)
        self.b8 = QtWidgets.QPushButton(Dialog)
        self.b8.setGeometry(QtCore.QRect(1097, 255, 90, 60))
        self.b8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.b8_clicked)
        self.b9 = QtWidgets.QPushButton(Dialog)
        self.b9.setGeometry(QtCore.QRect(1193, 255, 90, 60))
        self.b9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.b9_clicked)
        self.b4 = QtWidgets.QPushButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(1001, 323, 90, 60))
        self.b4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.b4_clicked)
        self.b5 = QtWidgets.QPushButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(1097, 323, 90, 60))
        self.b5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.b5_clicked)
        self.b6 = QtWidgets.QPushButton(Dialog)
        self.b6.setGeometry(QtCore.QRect(1193, 323, 90, 60))
        self.b6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.b6_clicked)
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(1001, 391, 90, 60))
        self.b1.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1_clicked)
        self.b2 = QtWidgets.QPushButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(1097, 391, 90, 60))
        self.b2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2_clicked)
        self.b3 = QtWidgets.QPushButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(1193, 391, 90, 60))
        self.b3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3_clicked)
        self.b0 = QtWidgets.QPushButton(Dialog)
        self.b0.setGeometry(QtCore.QRect(1001, 461, 90, 60))
        self.b0.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(self.b0_clicked)
        self.b00 = QtWidgets.QPushButton(Dialog)
        self.b00.setGeometry(QtCore.QRect(1097, 461, 90, 60))
        self.b00.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.b00.setObjectName("b00")
        self.b00.clicked.connect(self.b00_clicked)
        # 수량변경
        self.num_change = QtWidgets.QPushButton(Dialog)
        self.num_change.setGeometry(QtCore.QRect(1290, 255, 91, 91))
        self.num_change.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.num_change.setObjectName("num_change")
        self.num_change.clicked.connect(self.num_change_clicked)
        # 결제 완료 버튼
        self.pay_complt = QtWidgets.QPushButton(Dialog)
        self.pay_complt.setGeometry(QtCore.QRect(1290, 360, 91, 91))
        self.pay_complt.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pay_complt.setObjectName("pay_complt")
        self.pay_complt.clicked.connect(self.pay_complt_clicked)
        # Clear
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(1193, 461, 187, 60))
        self.clear.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.clear_clicked)
        # 결제내역조회
        self.detail_pay = QtWidgets.QPushButton(Dialog)
        self.detail_pay.setGeometry(QtCore.QRect(997, 530, 131, 175))
        self.detail_pay.setStyleSheet("border-image: url(:/newPrefix/pay_check.png);")
        self.detail_pay.setObjectName("detail_pay")
        self.detail_pay.clicked.connect(self.detail_pay_clicked)
        # 사용종료
        self.main_off = QtWidgets.QPushButton(Dialog)
        self.main_off.setGeometry(QtCore.QRect(1257, 530, 129, 175))
        self.main_off.setStyleSheet("border-image: url(:/newPrefix/exit.png);")
        self.main_off.setObjectName("main_off")
        self.main_off.clicked.connect(self.main_off_clicked)
        # 관리자모드
        self.ad_mode = QtWidgets.QPushButton(Dialog)
        self.ad_mode.setGeometry(QtCore.QRect(1126, 532, 131, 171))
        self.ad_mode.setStyleSheet("border-image: url(:/newPrefix/ad_mode.png);")
        self.ad_mode.setObjectName("ad_mode")
        self.ad_mode.clicked.connect(self.ad_mode_clicked)
        # 현금 결제
        self.money_pay = QtWidgets.QPushButton(Dialog)
        self.money_pay.setGeometry(QtCore.QRect(380, 505, 201, 200))
        self.money_pay.setStyleSheet("border-image: url(:/newPrefix/money.png);")
        self.money_pay.setObjectName("money_pay")
        self.money_pay.clicked.connect(self.money_pay_clicked)
        # 카드 결제
        self.card_pay = QtWidgets.QPushButton(Dialog)
        self.card_pay.setGeometry(QtCore.QRect(581, 505, 201, 200))
        self.card_pay.setStyleSheet("border-image: url(:/newPrefix/card.png);")
        self.card_pay.setObjectName("card")
        self.card_pay.clicked.connect(self.card_pay_clicked)
        # 상품권 결제
        self.gift = QtWidgets.QPushButton(Dialog)
        self.gift.setGeometry(QtCore.QRect(783, 505, 201, 200))
        self.gift.setStyleSheet("border-image: url(:/newPrefix/gift.png);")
        self.gift.setObjectName("gift")
        self.gift.clicked.connect(self.gift_pay_clicked)
        # 가운데 바코드 입력 칸
        self.barcode_input = QtWidgets.QLineEdit(Dialog)
        self.barcode_input.setGeometry(QtCore.QRect(278, 417, 621, 61))
        self.barcode_input.setStyleSheet("border-image: url(:/newPrefix/barcode.png);\n"
                                         "font: 28pt \"Arial\";")
        self.barcode_input.setText("")
        self.barcode_input.setObjectName("barcode_input")
        # 바코드 입력 버튼
        self.enter = QtWidgets.QPushButton(Dialog)
        self.enter.setGeometry(QtCore.QRect(900, 410, 75, 75))
        self.enter.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.enter.setObjectName("enter")
        self.enter.clicked.connect(self.enter_clicked)
        # 상품 리스트 칸
        self.list = QtWidgets.QTextEdit(Dialog)
        self.list.setGeometry(QtCore.QRect(30, 70, 941, 321))
        self.list.setStyleSheet("border-image: url(:/newPrefix/list.png);\n"
                                "font: 20pt \"Fixedsys\";")
        self.list.setObjectName("list")
        # 우측 상단
        # 총 매출액
        self.m1 = QtWidgets.QLineEdit(Dialog)
        self.m1.setGeometry(QtCore.QRect(1130, 33, 231, 31))
        self.m1.setStyleSheet("border-image: url(:/newPrefix/m.png);\n"
                              "font: 16pt \"Arial\";")
        self.m1.setText("0")
        self.m1.setObjectName("m1")
        # 할인금액
        self.m2 = QtWidgets.QLineEdit(Dialog)
        self.m2.setGeometry(QtCore.QRect(1130, 70, 231, 31))
        self.m2.setStyleSheet("font: 16pt \"Arial\";\n"
                              "border-image: url(:/newPrefix/m.png);")
        self.m2.setText("0")
        self.m2.setObjectName("m2")
        # 받을 금액
        self.m3 = QtWidgets.QLineEdit(Dialog)
        self.m3.setGeometry(QtCore.QRect(1130, 130, 231, 31))
        self.m3.setStyleSheet("font: 16pt \"Arial\";\n"
                              "border-image: url(:/newPrefix/m.png);")
        self.m3.setText("0")
        self.m3.setObjectName("m3")
        # 받은 금액
        self.m4 = QtWidgets.QLineEdit(Dialog)
        self.m4.setGeometry(QtCore.QRect(1130, 164, 231, 31))
        self.m4.setStyleSheet("border-image: url(:/newPrefix/m.png);\n"
                              "font: 16pt \"Arial\";")
        self.m4.setText("0")
        self.m4.setObjectName("m4")
        # 거스름돈
        self.m5 = QtWidgets.QLineEdit(Dialog)
        self.m5.setGeometry(QtCore.QRect(1130, 199, 231, 31))
        self.m5.setStyleSheet("border-image: url(:/newPrefix/m.png);\n"
                              "font: 16pt \"Arial\";")
        self.m5.setText("0")
        self.m5.setObjectName("m5")
        # 받은 금액 입력 // 우측 받은 금액 옆 V 표시 버튼
        self.enter2 = QtWidgets.QPushButton(Dialog)
        self.enter2.setGeometry(QtCore.QRect(1320, 160, 50, 50))
        self.enter2.setStyleSheet("border-image: url(image/enter2.png);")
        self.enter2.setObjectName("enter2")
        self.enter2.clicked.connect(self.enter2_clicked)
        # 왼쪽 하단 알림
        self.alarm = QtWidgets.QLineEdit(Dialog)
        self.alarm.setGeometry(QtCore.QRect(20, 580, 271, 61))
        self.alarm.setStyleSheet("border-image: url(:/newPrefix/time.png);\n"
                                "font: 28pt \"Arial\";")
        self.alarm.setText("")
        self.alarm.setObjectName("alarm")

        # 결제 내역 조회 버튼 선언
        # 결제 내역 조회 라벨
        self.detail_pay_bg = QtWidgets.QLabel(Dialog)
        self.detail_pay_bg.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.detail_pay_bg.setPixmap(QtGui.QPixmap("image/detail_pay_bg.png"))
        self.detail_pay_bg.setScaledContents(True)
        self.detail_pay_bg.setObjectName("detail_pay_bg")
        #결제 내역 조회
        self.pay_detailpay = QtWidgets.QPushButton(Dialog)
        self.pay_detailpay.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.pay_detailpay.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pay_detailpay.setObjectName("pay_detailpay")
        self.pay_detailpay.clicked.connect(self.pay_detailpay_clicked)
        # 영수증 조회
        self.receipt_check = QtWidgets.QPushButton(Dialog)
        self.receipt_check.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.receipt_check.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.receipt_check.setObjectName("receipt_check")
        self.receipt_check.clicked.connect(self.receipt_check_clicked)
        # 영수증 출력
        self.receipt_print = QtWidgets.QPushButton(Dialog)
        self.receipt_print.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.receipt_print.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.receipt_print.setObjectName("receipt_print")
        self.receipt_print.clicked.connect(self.receipt_print_clicked)
        # 돌아가기
        self.payment_off = QtWidgets.QPushButton(Dialog)
        self.payment_off.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.payment_off.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.payment_off.setObjectName("payment_off")
        self.payment_off.clicked.connect(self.payment_off_clicked)
        # 결제 취소
        self.payment_cancle = QtWidgets.QPushButton(Dialog)
        self.payment_cancle.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.payment_cancle.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.payment_cancle.setObjectName("payment_cancle")
        self.payment_cancle.clicked.connect(self.payment_cancle_clicked)

        # 관리자 모드 버튼 선언
        # 관리자 모드 버튼
        self.ad_bottom = QtWidgets.QPushButton(Dialog)
        self.ad_bottom.setStyleSheet("border-image: url(image/ad_bottom.png);\n")
        self.ad_bottom.setObjectName("ad_bottom")
        self.ad_bottom.setGeometry(QtCore.QRect(0, 0, 0, 0))

        # 관리자모드 상단 라벨
        self.ad_top = QtWidgets.QPushButton(Dialog)
        self.ad_top.setStyleSheet("border-image: url(image/ad_top.png);\n")
        self.ad_top.setObjectName("ad_top")
        self.ad_top.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # 입고 버튼
        self.goods_input = QtWidgets.QPushButton(Dialog)
        self.goods_input.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_input.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.goods_input.setObjectName("goods_input")
        self.goods_input.clicked.connect(self.goods_input_clicked)
        # 수정 버튼
        self.goods_modification = QtWidgets.QPushButton(Dialog)
        self.goods_modification.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_modification.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.goods_modification.setObjectName("goods_modification")
        self.goods_modification.clicked.connect(self.goods_modification_clicked)
        # 폐기 버튼
        self.goods_delete = QtWidgets.QPushButton(Dialog)
        self.goods_delete.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_delete.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.goods_delete.setObjectName("goods_delete")
        self.goods_delete.clicked.connect(self.goods_delete_clicked)
        # 행사상품 버튼
        self.event_product = QtWidgets.QPushButton(Dialog)
        self.event_product.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.event_product.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.event_product.setObjectName("event_product")
        self.event_product.clicked.connect(self.event_product_clicked)
        #결제 내역 조회 버튼
        self.detail_pay = QtWidgets.QPushButton(Dialog)
        self.detail_pay.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.detail_pay.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.detail_pay.clicked.connect(self.detail_pay_clicked)
        #재고 조회 버튼
        self.stock = QtWidgets.QPushButton(Dialog)
        self.stock.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.stock.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.stock.setObjectName("stock")
        self.stock.clicked.connect(self.stock_clicked)
        #직원 모드 버튼
        self.staff_mode = QtWidgets.QPushButton(Dialog)
        self.staff_mode.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.staff_mode.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.staff_mode.setObjectName("staff_mode")
        self.staff_mode.clicked.connect(self.staff_mode_clicked)
        #매출 조회 버튼
        self.ad_sales = QtWidgets.QPushButton(Dialog)
        self.ad_sales.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_sales.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.ad_sales.setObjectName("ad_sales")
        self.ad_sales.clicked.connect(self.ad_sales_clicked)
        #사용 종료 버튼
        self.ad_off = QtWidgets.QPushButton(Dialog)
        self.ad_off.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_off.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.ad_off.setObjectName("ad_off")
        self.ad_off.clicked.connect(self.main_off_clicked)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 첫 화면 버튼 클릭 이벤트
    def b0_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '0'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '0'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "0")
        else:
            self.m4.setText(self.m4.text() + "0")

    def b1_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '1'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '1'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "1")
        else:
            self.m4.setText(self.m4.text() + "1")

    def b2_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '2'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '2'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "2")
        else:
            self.m4.setText(self.m4.text() + "2")

    def b3_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '3'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '3'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "3")
        else:
            self.m4.setText(self.m4.text() + "3")

    def b4_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '4'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '4'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "4")
        else:
            self.m4.setText(self.m4.text() + "4")

    def b5_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '5'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '5'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "5")
        else:
            self.m4.setText(self.m4.text() + "5")

    def b6_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '6'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '6'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "6")
        else:
            self.m4.setText(self.m4.text() + "6")

    def b7_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '7'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '7'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "7")
        else:
            self.m4.setText(self.m4.text() + "7")

    def b8_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '8'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '8'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "8")
        else:
            self.m4.setText(self.m4.text() + "8")

    def b9_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '9'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '9'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "9")
        else:
            self.m4.setText(self.m4.text() + "9")

    def b00_clicked(self):
        '''
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)에 '00'을 추가함
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)에 '00'을 추가함
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText(self.barcode_input.text() + "00")
        else:
            self.m4.setText(self.m4.text() + "00")

    def clear_clicked(self):
        '''
        'Clear' 버튼 클릭 이벤트
        self.__target_barcode is True : 바코드 입력칸(self.barcode_input)을 ''(빈 문자열)로 설정
        self.__target_barcode is False : 왼쪽 상단 받은 금액칸(self.m4)을 ''(빈 문자열)로 설정
        :return:
        '''
        if self.__target_barcode:
            self.barcode_input.setText("")
        else:
            self.m4.setText("")

    def pay_complt_clicked(self):
        '''
        '결제 완료' 버튼 클릭 이벤트
        self.__mode가 'main'일 때, 현금 결제 시 완료 버튼이다.
        결제 정보를 저장하고, 결제 목록을 재고에서 뺀 후, 영수증(메모장을 띄움)을 출력함
        :return:
        '''
        if self.__mode == 'pay':
            self.common_function.msg_box('이 화면에서는 지원하지 않는 버튼입니다.     ')
            return

        if self.m4.text() == '' or self.m4.text() == '0' or self.m5.text() == '' or self.__target_barcode == True:
            self.common_function.msg_box('받은 금액을 입력하시오.     ')
            return

        #결제 정보를 저장하기 위해 DB로 보냄
        temp = self.common_function.result_print(self.__list_buf)
        self.__reset_money(temp[0], temp[1], temp[2], temp[3], temp[4])
        total_price = temp[2]
        payment_number = self.set_payment_info.set_payment_number()
        now = self.set_payment_info.read_datetime()
        self.set_payment_info.send_payment_result(payment_number, now, '현금', '-', total_price)
        self.__list_buf = self.common_function.modify_list_buf(self.__list_buf)
        self.set_payment_info.send_payment_detail(self.__list_buf, payment_number)

        #결제한 수량을 재고에서 뺌
        for i in self.__list_buf:
            pro = self.stock_manager.product_search(i[0])
            self.stock_manager.product_quan_modification(i[0], int(pro[2]) - int(i[3]))
        self.common_function.msg_box('결제가 완료되었습니다.     ')

        #영수증 출력 후 화면 리셋
        last_receipt_number = int(self.set_payment_info.set_payment_number()) - 1
        detail = self.payment_manager.return_detail(str(last_receipt_number))
        now = datetime.now()
        date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        self.common_function.receipt_print_form(date,detail,last_receipt_number)
        self.m5.setText(self.common_function.insert_comma((self.m5.text())))
        self.__target_barcode = True
        self.__print_reset()

    def num_change_clicked(self):
        '''
        '수량 변경' 버튼 클릭 이벤트
        새로운 GUI 윈도우를 띄워서 번호와 수량을 입력받아와서 현재보이는 리스트를 수정함.
        - self.__mode 가 'main'이면 결제 리스트 수정
        - self.__mode 가 'admin'이면 재고 리스트 수정
        :return:
        '''
        if self.__mode == 'main' and len(self.__list_buf) == 0:
            self.common_function.msg_box('상품을 입력하시오.     ')
            return
        elif self.__event_print_check == True:
            pass
        elif self.__mode == 'admin' and self.__change_check == False:
            self.common_function.msg_box('재고조회를 먼저 하시오.     ')
            return
        elif self.__mode == 'pay':
            self.common_function.msg_box('이 화면에서는 수량변경을 할 수 없습니다.     ')
            return
        # 수량 변경(새로운 GUI Window)창을 띄움
        Dialog = QtWidgets.QDialog()
        dlg = Count_modification()
        if self.__mode == 'main':
            main_mode = True
        else:
            main_mode = False
        dlg.setupUi(Dialog,main_mode)
        Dialog.show()
        Dialog.exec_()

        if self.__mode == 'main':
            num, cnt = self.__num_cnt_to_text(self.common_function.text_read('text/count_modification_buf.txt'))
            if int(num) > len(self.__list_buf) or int(num) < 1:
                self.__text_reset('text/count_modification_buf.txt')
                return
            else:
                self.__main_quantity_modification(num, cnt)
                if int(cnt) == 0:
                    self.__list_buf.pop(int(num)-1)
                self.__list_print()
        elif self.__mode == 'admin' and self.__event_print_check == True:
            num, cnt = self.__num_cnt_to_text(self.common_function.text_read('text/count_modification_buf.txt'))
            st = Stock_management()
            stock_list = st.product_event_list()
            if int(num) > len(stock_list) or int(num) < 1:
                self.__text_reset('text/count_modification_buf.txt')
                return
            else:
                barcode = stock_list[int(num)-1][0]
                self.stock_manager.product_quan_modification(barcode, int(cnt))
                self.__event_product_list_print()
        elif self.__mode == 'admin' and self.__event_print_check == False:
            num, cnt = self.__num_cnt_to_text(self.common_function.text_read('text/count_modification_buf.txt'))
            stock_list = self.stock_manager.product_check()
            if int(num) > len(stock_list) or int(num) < 1:
                self.__text_reset('text/count_modification_buf.txt')
                return
            else:
                barcode = stock_list[int(num)-1][0]
                self.stock_manager.product_quan_modification(barcode, int(cnt))
                self.__stock_print(self.stock_manager.product_check())
        self.__text_reset('text/count_modification_buf.txt')

    def money_pay_clicked(self):
        '''
        '현금' 버튼 클릭 이벤트
        self.__target_barcode를 False로 바꾸고 받은 금액을 입력받을 준비를 함.
        :return:
        '''
        if len(self.__list_buf) == 0:
            self.common_function.msg_box('상품을 입력하시오.     ')
            return

        self.__target_barcode = False
        self.common_function.msg_box('받은 금액을 입력하시오.     ')
        self.m4.setText("")

    def card_pay_clicked(self):
        '''
        '카드' 버튼 클릭 이벤트
        카드결제를 하기위한 새로운 GUI Window를 띄우고 결제가 완료 되었다면 화면을 리셋함
        :return:
        '''
        if len(self.__list_buf) == 0:
            self.common_function.msg_box('상품을 입력하시오.     ')
            return

        #그냥 창을 열고 닫았는지, 기능을 했는지 체크 하기 위함
        buf = None
        with open('text/card_check.txt', 'r', encoding='utf-8') as f:
            if f is not None:
                buf = f.read()

        #카드 번호를 입력받을 새로운 GUI Window 창을 띄움
        Dialog = QtWidgets.QDialog()
        dlg = Card_payment()
        dlg.setupUi(Dialog, self.__list_buf)
        Dialog.show()
        Dialog.exec_()

        #결제가 완료 되었다면, 파일의 값이 바뀐것이므로 화면을 리셋함
        check = True
        with open('text/card_check.txt', 'r', encoding='utf-8') as f:
            if buf == f.read() or buf == None:
                check = False
        if check == False:
            return
        else:
            self.__print_reset()

    def gift_pay_clicked(self):
        '''
        '상품권' 버튼 클릭 이벤트
        상품권결제를 하기위한 새로운 GUI Window를 띄우고 결제가 완료 되었다면 화면을 리셋함
        :return:
        '''
        if len(self.__list_buf) == 0:
            self.common_function.msg_box('상품을 입력하시오.     ')
            return
        elif len(self.__list_buf) > 1:
            self.common_function.msg_box('상품권 결제는 단일상품만 가능합니다.     ')
            return
        # 상품권 번호를 입력받을 새로운 GUI Window 창을 띄움
        buf = None
        with open('text/card_check.txt', 'r', encoding='utf-8') as f:
            if f is not None:
                buf = f.read()

        # 상품권 번호를 입력받을 새로운 GUI Window 창을 띄움
        Dialog = QtWidgets.QDialog()
        dlg = Giftcard_payment()
        dlg.setupUi(Dialog, self.__list_buf)
        Dialog.show()
        Dialog.exec_()

        # 결제가 완료 되었다면, 파일의 값이 바뀐것이므로 화면을 리셋함
        check = True
        with open('text/giftcard_check.txt', 'r', encoding='utf-8') as f:
            if buf == f.read() or buf == None:
                check = False
        if check == False:
            return
        else:
            self.__print_reset()

    def enter2_clicked(self):
        '''
        받은 금액 옆의 'V' 버튼 클릭 이벤트
        받은 금액을 입력받고, 거스름돈을 계산하고 출력함
        :return:
        '''
        get_money = self.m4.text()
        if get_money == '':
            self.common_function.msg_box('받은 금액을 입력하시오.      ')
            return

        temp = self.common_function.result_print(self.__list_buf)
        self.__reset_money(temp[0], temp[1], temp[2], temp[3], temp[4])
        total_money = temp[2]
        if int(get_money) - int(total_money) < 0:
            self.common_function.msg_box('금액이 부족합니다.     ')
            self.m4.setText("")
            return

        if get_money != '0' and get_money != '' and self.__target_barcode == False:
            if int(get_money) - int(total_money) >= 0:
                self.m4.setText(self.common_function.insert_comma(get_money))
                self.m5.setText(self.common_function.insert_comma(str(int(get_money) - int(total_money))))
            else:
                self.common_function.msg_box('금액이 부족합니다.     ')

    def enter_clicked(self):
        '''
        바코드 입력 칸 옆 입력 버튼 클릭 이벤트
        self.__mode 가 'main'이면 결제 상품 리스트에 추가
        self.__mode 가 'admin'이면 재고 검색
        self.__mode 가 'pay'이면 지원하지않는다는 알림창
        :return:
        '''
        if self.__mode == 'pay':
            self.common_function.msg_box('이 화면에서는 바코드를 입력할 수 없습니다.     ')
            return

        #바코드 찍는 소리
        barcode = self.barcode_input.text()
        self.barcode_input.setText("")
        winsound.Beep(1800, 200)
        #재고리스트를 가져옴
        product_list = self.stock_manager.product_check()
        check = False
        #재고리스트에 있는지 없는지 체크
        for product_info in product_list:
            if str(product_info[0]) == barcode:
                check = True
                break
        if check == False:
            self.common_function.msg_box("존재하지 않는 바코드입니다 !")
            return

        product_info = self.stock_manager.product_search(barcode)    #바코드로 상품을 검색함 // product_info = [barcode, name, quantity, price, event, minor]
        #self.__mode 가 'main'이면 상품 리스트에 추가함
        if self.__mode == 'main':
            if len(self.__list_buf) == 0:
                self.__add1_list(product_info[0], product_info[1], str(product_info[3]),
                               product_info[4], product_info[5])
            else:
                self.__add2_list(product_info[0], product_info[1], str(product_info[3]),
                               product_info[4], product_info[5])
            self.__list_print()
            if product_info[4] == '1+1' or product_info[4] == '2+1':
                self.common_function.msg_box('행사상품입니다. 수량을 확인하세요.     ')
        #self.__mode 가 'admin'이면 재고를 검색함
        elif self.__mode == 'admin':
            stock_list = [[product_info[0],product_info[1],product_info[2],product_info[3],product_info[5],product_info[4]]]
            self.__last_product = stock_list
            stock_list[0][4] , stock_list[0][5] = stock_list[0][5], stock_list[0][4]
            self.__stock_print(self.__last_product)
            self.__change_check = False
        else:
            self.common_function.msg_box('지원하지 않는 모드입니다.     ')

    def main_off_clicked(self):
        '''
        '사용종료' 버튼 클릭 이벤트
        프로그램을 종료함
        :return:
        '''
        sys.exit()

    def ad_mode_clicked(self):
        '''
        '관리자 모드' 버튼 클릭 이벤트
        관리자 모드로 전환함
        :return:
        '''
        self.__mode = 'admin'
        self.__change_check = False
        self.__event_print_check = False
        self.__print_reset()

        self.bg.setPixmap(QtGui.QPixmap("image/POSadm.png"))
        self.event_product.setGeometry(QtCore.QRect(1290, 360, 91, 91))
        self.ad_bottom.setGeometry(QtCore.QRect(998, 525, 387, 185))
        self.ad_top.setGeometry(QtCore.QRect(998, 20, 387, 225))
        self.goods_input.setGeometry(QtCore.QRect(1001, 160, 122, 83))
        self.goods_modification.setGeometry(QtCore.QRect(1129, 160, 122, 83))
        self.goods_delete.setGeometry(QtCore.QRect(1256, 160, 122, 83))
        self.detail_pay.setGeometry(QtCore.QRect(1003, 531, 122, 169))
        self.stock.setGeometry(QtCore.QRect(1132, 531, 122, 81))
        self.staff_mode.setGeometry(QtCore.QRect(1260, 531, 122, 81))
        self.ad_sales.setGeometry(QtCore.QRect(1132, 620, 122, 81))
        self.ad_off.setGeometry(QtCore.QRect(1260, 620, 122, 81))

    def detail_pay_clicked(self):
        '''
        '결제내역관리'버튼 클릭 이벤트 (self.__mode == 'main'일 때,)
        결제내역관리 화면으로 전환함
        :return:
        '''
        self.bg.setPixmap(QtGui.QPixmap("image/payment_bg.png"))
        self.__mode = 'pay'
        self.__change_check = False
        self.__receipt_buf = None
        self.__print_reset()

        self.event_product.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_bottom.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_top.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_input.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_modification.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_delete.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.detail_pay.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.stock.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.staff_mode.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_sales.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_off.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.detail_pay_bg.setGeometry(QtCore.QRect(997, 527, 390, 178))
        self.pay_detailpay.setGeometry(QtCore.QRect(1001, 531, 122, 169))
        self.receipt_check.setGeometry(QtCore.QRect(1129, 531, 122, 81))
        self.receipt_print.setGeometry(QtCore.QRect(1129, 620, 122, 81))
        self.payment_off.setGeometry(QtCore.QRect(1256, 620, 122, 81))
        self.payment_cancle.setGeometry(QtCore.QRect(1256, 531, 122, 81))

    #결제 내역 조회 눌렀을 때 화면 버튼 이벤트
    def receipt_check_clicked(self):
        '''
        '영수증 조회'버튼 클릭 이벤트
        영수증 조회를 위한 새로운 GUI Window를 띄우고 조회가 되었으면 출력함
        :return:
        '''
        check_num = None
        text = self.common_function.text_read('text/receipt_search_buf.txt')
        if text != '':
            check = True
            text = text.split('\n')
            check_num = str(int(text[0]))

        Dialog = QtWidgets.QDialog()
        dlg = Receipt_search()
        dlg.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

        check = False

        text = self.common_function.text_read('text/receipt_search_buf.txt')
        if text != '':
            check = True
            text = text.split('\n')
            check_num2 = str(text[0])

        if check == False or check_num == None:
            return

        if check_num == check_num2:
            return
        else:
            text = text[1].split('#')
            paylist = [text[0:-1]]
            self.__receipt_buf = paylist[0][0]
            self.__detail_pay_print_in_payment_mode(paylist)

    def event_product_clicked(self):
        '''
        '행사상품' 버튼 클릭 이벤트
        self.evnet_product_list_pinrt() 호출 (행사상품 리스트만 출력)
        :return:
        '''
        self.__event_print_check = True
        self.__event_product_list_print()

    def pay_detailpay_clicked(self):
        '''
        '결제 내역 조회' 버튼 클릭 이벤트 (self.__mode == 'pay'일 때,)
        결제 내역을 출력함
        :return:
        '''
        paylist = self.payment_manager.check_payment()
        self.__detail_pay_print_in_payment_mode(paylist)

    def receipt_print_clicked(self):
        '''
        '영수증 출력'버튼 클릭 이벤트
        조회된 영수증을 출력함
        :return:
        '''
        if self.__receipt_buf == None:
            self.common_function.msg_box('영수증을 먼저 조회하시오.     ')
            return
        detail = self.payment_manager.return_detail(str(self.__receipt_buf))
        text = text = self.common_function.text_read('text/receipt_search_buf.txt').split('\n')
        text = text[1].split('#')
        date = text[1]
        self.common_function.receipt_print_form(date,detail,self.__receipt_buf)

    def payment_cancle_clicked(self):
        '''
        '결제취소'버튼 클릭 이벤트
        조회된 영수증 내용을 취소함 (카드, 현금은 취소 // 상품권은 취소 불가능)
        조회된 영수증이 카드결제로 결제가 되었다면, 카드번호를 받는 새로운 GUI Window 창을 띄움
        받아온 카드 번호와 조회된 카드번호가 일치하면 취소함
        :return:
        '''
        if self.__receipt_buf == None:
            self.common_function.msg_box('영수증을 먼저 조회하시오.     ')
            return
        #영수증 바코드로 DB에서 내용을 읽어옴
        payment_list = self.payment_manager.check_barcode(self.__receipt_buf)
        method = payment_list[2]
        # '카드결제'라면 카드 번호를 받아서 확인함
        if method == '카드':
            check_num = None
            text = self.common_function.text_read('text/card_cancle.txt')
            if text == '' or text is None:
                check_num = '1'
            else:
                text = text.split('\n')
                check_num = str(int(text[0]) + 1)
            #새로운 GUI Window 창을 띄움
            Dialog = QtWidgets.QDialog()
            dlg = Card_cancle()
            dlg.setupUi(Dialog)
            Dialog.show()
            Dialog.exec_()

            check_num2 = None

            text = self.common_function.text_read('text/card_cancle.txt')
            if text == '':
                check_num2 = False
            else:
                text = text.split('\n')
                card_num , check_num2 = str(text[1]) , str(int(text[0]))
            if check_num != check_num2:
                return
            method_info = str(payment_list[3])
            if card_num == method_info:
                pay_num = payment_list[0]
                pro_list = self.payment_manager.return_detail(pay_num)
                for i in pro_list:
                    pro = self.stock_manager.product_search(i[6])
                    self.stock_manager.product_quan_modification(i[6], int(pro[2]) + int(i[1]))
                self.payment_manager.remove_payment(str(self.__receipt_buf))
                self.payment_manager.remove_payment_detail(str(self.__receipt_buf))
                self.__receipt_buf = None
                self.list.setText("")
                self.common_function.msg_box('취소되었습니다.     ')
            else:
                self.__receipt_buf = None
                self.list.setText("")
                self.common_function.msg_box('카드번호가 일치하지 않습니다.     ')
        elif method == '현금':
            pay_num = payment_list[0]
            pro_list = self.payment_manager.return_detail(pay_num)
            for i in pro_list:
                pro = self.stock_manager.product_search(i[6])
                self.stock_manager.product_quan_modification(i[6], int(pro[2]) + int(i[1]))
            self.payment_manager.remove_payment(str(self.__receipt_buf))
            self.payment_manager.remove_payment_detail(str(self.__receipt_buf))
            self.common_function.msg_box('취소되었습니다.     ')
            self.list.setText("")
        else:
            self.common_function.msg_box('상품권은 취소되지 않습니다.     ')
            self.list.setText("")
        self.__change_check = False

    def payment_off_clicked(self):
        '''
        '돌아가기'버튼 클릭 이벤트
        프로그램 첫 화면으로 돌아감
        :return:
        '''
        self.bg.setPixmap(QtGui.QPixmap("image/back_ground.png"))
        self.__receipt_buf = None
        self.__mode = 'main'
        self.__print_reset()

        self.detail_pay_bg.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.pay_detailpay.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.receipt_check.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.receipt_print.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.payment_off.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.payment_cancle.setGeometry(QtCore.QRect(0, 0, 0, 0))


    # 관리자 모드 눌렀을 때 화면 버튼 이벤트
    def goods_input_clicked(self):
        '''
        '입고' 버튼 클릭 이벤트
        입고를 위한 새로운 GUI Window를 띄우고 수정된 재고를 출력함
        :return:
        '''
        Dialog = QtWidgets.QDialog()
        dlg = Goods_input()
        dlg.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

        self.__stock_print(self.stock_manager.product_check())

    def goods_modification_clicked(self):
        '''
        '수정' 버튼 클릭 이벤트
        조회된 재고를 수정하는 새로운 GUI Window를 띄우고 수정된 재고를 출력함
        :return:
        '''
        if self.__last_product == None:
            self.common_function.msg_box('바코드를 입력하시오.     ')
            return
        Dialog = QtWidgets.QDialog()
        dlg = Goods_modification()
        dlg.setupUi(Dialog,self.__last_product[0][0])
        Dialog.show()
        Dialog.exec_()

        self.__last_product = None
        self.__stock_print(self.stock_manager.product_check())

    def goods_delete_clicked(self):
        '''
        '폐기' 버튼 클릭 이벤트
        조회된 재고를 수량을 0으로 하지만, 다른 정보를 지우지는 않음
        :return:
        '''
        if self.__last_product == None:
            self.common_function.msg_box('바코드를 입력하시오.     ')
            return
        else:
            barcode = self.__last_product[0][0]
            self.stock_manager.product_quan_modification(barcode,0)
            self.common_function.msg_box('폐기되었습니다.     ')
            self.__last_product = None
            self.__stock_print(self.stock_manager.product_check())

    def staff_mode_clicked(self):
        '''
        '직원 모드' 버튼 클릭 이벤트
        프로그램 첫 화면으로 전환함
        :return:
        '''
        self.__mode = 'main'
        self.__print_reset()

        self.bg.setPixmap(QtGui.QPixmap("image/back_ground.png"))
        self.event_product.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_bottom.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_top.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_input.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_modification.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.goods_delete.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.detail_pay.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.stock.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.staff_mode.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_sales.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ad_off.setGeometry(QtCore.QRect(0, 0, 0, 0))

    def stock_clicked(self):
        '''
        '재고 조회' 버튼 클릭 이벤트
        DB에서 재고를 조회해서 출력함
        :return:
        '''
        stock_list = self.stock_manager.product_check()
        self.__stock_print(stock_list)
        self.__event_print_check = False
        self.__change_check = True

    def ad_sales_clicked(self):
        '''
        '매출 조회' 버튼 클릭 이벤트
        매출 조회를 할 새로운 GUI Window 창을 띄움
        :return:
        '''
        Dialog = QtWidgets.QDialog()
        dlg = Sales_check()
        dlg.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    # 함수에서 호출되는 함수들
    def __detail_pay_print_in_payment_mode(self,pay_list):
        '''
        pay_list 를 출력 전에 전처리 후, 출력하는 함수로 넘김
        :param pay_list: [[영수증번호, 결제시각, 결제수단, 결제수단정보, 총액], ...]
        :return:
        '''
        buf = self.list_print_function.detail_pay_return_in_payment_mode(pay_list)
        self.list.setText(buf)

    def __event_product_list_print(self):
        '''
        DB에서 evnet_type이 null이 아닌 상품만 가져와서 self.__stock_print에 넘김
        :return:
        '''
        stock_list = self.stock_manager.product_event_list()
        self.__stock_print(stock_list)

    def __stock_print(self, stock_list):
        '''
        재고를 화면에 맞게 출력함
        :param pay_list: list - [[영수증번호, 결제시각, 결제수단, 결제수단정보, 총액], ...]
        :return:
        '''
        buf = ''

        n = 1
        for one_line in stock_list:
            barcode, name, quantity,price, event, minor = str(one_line[0]), str(one_line[1]), str(one_line[2]), str(one_line[3]), str(one_line[4]), str(one_line[5])
            if n < 10:
                num = '0' + str(n)
            else:
                num = str(n)
            n += 1
            if event == 'None':
                event = ''
            buf += self.list_print_function.number_print(num) + barcode + ' '*13 + self.list_print_function.name_print(name) +  self.list_print_function.price_print(price) + self.list_print_function.count_print(quantity) + self.list_print_function.minor_print(minor) + self.list_print_function.event_print(event) + '\n'
        self.list.setText(buf)

    def __main_quantity_modification(self, num, cnt):
        '''
        self.__list_buf의 수량과 총금액을 수정함
        :param num: int - 출력 되어 있는 상품 리스트 번호
        :param cnt: int - 변경될 수량
        :return:
        '''
        index = int(num) - 1
        self.__list_buf[index][3] = cnt
        self.__list_buf[index][4] = int(self.__list_buf[index][2]) * int(self.__list_buf[index][3])

    def __text_reset(self,file_name):
        '''
        파일을 '-1 -1'로 리셋함
        :param file_name: File - reset 될 파일 경로
        :return:
        '''
        self.common_function.text_write(file_name,'-1 -1')

    def __num_cnt_to_text(self,text):
        '''
        text를 split 하여 리턴함
        :param text: string - ex) 1 2 // 10 2 // 3 10
        :return: list - [num,cnt]
        '''
        text = text.split()
        return [text[0],text[1]]

    def __add1_list(self, barcode, name, price, event, minor):
        '''
        self.__list_buf에 없는 상품일 때, 새롭게 추가함 -> 수량 : 1
        :param barcode: string
        :param name: string
        :param price: string
        :param event: string
        :param minor: string
        :return:
        '''
        a = [barcode, name, int(price), 1, int(price), event]
        if str(minor) == '1':
            self.alarm.setText("신분증 확인 !!")

        self.__list_buf.append(a)

    def __add2_list(self, barcode, name, price, event, minor):
        '''
        self.__list_buf에 있는 상품일 때, 수량을 1 증가시키고 총 금액을 수정함
        :param barcode: string
        :param name: string
        :param price: string
        :param event: string
        :param minor: string
        :return:
        '''
        for i in range(len(self.__list_buf)):
            if barcode == self.__list_buf[i][0]:
                self.__list_buf[i][3] = int(self.__list_buf[i][3]) + 1
                self.__list_buf[i][4] = int(self.__list_buf[i][3]) * int(self.__list_buf[i][2])
                break

            if i == len(self.__list_buf) - 1:
                self.__add1_list(barcode, name, price, event, minor)

    def __list_print(self):
        '''
        결제 상품 목록을 출력함
        :return:
        '''
        text = ''
        n = 1
        for i in self.__list_buf:
            if int(i[3]) > 0:
                if n < 10:
                    num = '0' + str(n)
                else:
                    num = str(n)
                buf = num + ' ' * 9 + str(i[0]) + ' ' * 13 + self.list_print_function.name_print(i[1]) + self.list_print_function.price_print(i[2]) + self.list_print_function.count_print(i[3]) + self.list_print_function.price_print(i[4]) + self.list_print_function.event_print(i[5]) + '\n'
                text += buf
                n += 1

        self.list.setText(text)
        temp = self.common_function.result_print(self.__list_buf)
        self.__reset_money(temp[0], temp[1], temp[2], temp[3], temp[4])

    def __reset_money(self, m1_text, m2_text, m3_text, m4_text, m5_text):
        '''
        우측 상단의 금액 목록들을 세팅함
        :param m1_text: self.m1 에 쓸 text
        :param m2_text: self.m2 에 쓸 text
        :param m3_text: self.m3 에 쓸 text
        :param m4_text: self.m4 에 쓸 text
        :param m5_text: self.m5 에 쓸 text
        :return:
        '''
        m1_text, m2_text, m3_text, m4_text, m5_text = self.common_function.insert_comma(m1_text), self.common_function.insert_comma(m2_text), self.common_function.insert_comma(m3_text), self.common_function.insert_comma(m4_text), self.common_function.insert_comma(
            m5_text)
        self.m1.setText(m1_text)
        self.m2.setText(m2_text)
        self.m3.setText(m3_text)
        self.m4.setText(m4_text)
        self.m5.setText(m5_text)

    def __print_reset(self):
        '''
        모든 출력을 리셋함
        :return:
        '''
        self.list.setText("")
        self.__reset_money(0, 0, 0, 0, 0)
        self.__list_buf = []
        self.alarm.setText("")
        self.barcode_input.setText("")
import img_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
