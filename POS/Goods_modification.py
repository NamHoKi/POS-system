# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lacuc\Desktop\3\3-2\소공\폴더\guiui\gui\goodsmodify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Common_function import Common_function
from Stock_management import Stock_management

class Goods_modification(object):
    def setupUi(self, Dialog,last_barcode):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("POS")
        Dialog.setWindowIcon(QIcon('image/icon.png'))
        Dialog.resize(883, 923)

        self.__last_barcode = last_barcode
        self.common_function = Common_function()
        
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        #배경 라벨
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 883, 923))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/goods_modification.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        #이름 칸
        self.lgoodsname = QtWidgets.QLineEdit(self.centralwidget)
        self.lgoodsname.setGeometry(QtCore.QRect(324, 276, 466, 60))
        self.lgoodsname.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lgoodsname.setObjectName("lgoodsname")
        #바코드 칸
        self.lbarcode = QtWidgets.QLineEdit(self.centralwidget)
        self.lbarcode.setGeometry(QtCore.QRect(324, 188, 466, 60))
        self.lbarcode.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lbarcode.setObjectName("lbarcode")
        #미성년자구분 칸
        self.lgoodslimit = QtWidgets.QLineEdit(self.centralwidget)
        self.lgoodslimit.setGeometry(QtCore.QRect(324, 720, 466, 60))
        self.lgoodslimit.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lgoodslimit.setObjectName("lgoodslimit")
        #단가 칸
        self.lgoodsprice = QtWidgets.QLineEdit(self.centralwidget)
        self.lgoodsprice.setGeometry(QtCore.QRect(324, 366, 466, 60))
        self.lgoodsprice.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lgoodsprice.setObjectName("lgoodsprice")
        #완료 칸
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(536, 800, 126, 85))
        self.ok.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.ok_clicked)
        #수량 칸
        self.lgoodscnt = QtWidgets.QLineEdit(self.centralwidget)
        self.lgoodscnt.setGeometry(QtCore.QRect(324, 455, 466, 60))
        self.lgoodscnt.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lgoodscnt.setObjectName("lgoodscnt")
        #이벤트 칸
        self.lgoodsevent = QtWidgets.QLineEdit(self.centralwidget)
        self.lgoodsevent.setGeometry(QtCore.QRect(324, 632, 466, 60))
        self.lgoodsevent.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(image/fr5.png);\n"
                                     "font: 28pt \"Arial\";")
        self.lgoodsevent.setObjectName("lgoodsevent")
        #지우기 칸
        self.delet = QtWidgets.QPushButton(self.centralwidget)
        self.delet.setGeometry(QtCore.QRect(200, 800, 126, 85))
        self.delet.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.delet.setObjectName("delet")
        self.delet.clicked.connect(self.delete_clicked)
        #금액 칸
        self.ltotal = QtWidgets.QPushButton(self.centralwidget)
        self.ltotal.setGeometry(QtCore.QRect(324, 542, 466, 60))
        self.ltotal.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                  "border-image: url(image/fr5.png);\n"
                                  "font: 28pt \"Arial\";")
        self.ltotal.setObjectName("ltotal")
        self.ltotal.clicked.connect(self.ltotal_clicked)

    def ltotal_clicked(self):
        '''
        단가 x 수량 값을 self.ltotal에 출력함
        :return:
        '''
        price = self.lgoodsprice.text()
        cnt = self.lgoodscnt.text()
        text = int(price) * int(cnt)
        self.ltotal.setText(str(text))

    def ok_clicked(self):
         '''
         수정 될 조건들을 체크하고 모두 만족하면 수정함
         :return:
         '''
         barcode = self.lbarcode.text()
         name = self.lgoodsname.text()
         price = self.lgoodsprice.text()
         cnt = self.lgoodscnt.text()
         total = self.ltotal.text()
         event = self.lgoodsevent.text()
         limit = self.lgoodslimit.text()

         stock_manager = Stock_management()
         stock_list = stock_manager.product_check()

         for barcode_check in stock_list:
            if str(barcode_check[0]) == barcode and (self.__last_barcode != barcode_check[0]):
                self.common_function.msg_box('이미 존재하는 바코드입니다.     ')
                return

         if not self.common_function.check_barcode(barcode):
             return

         if not self.common_function.check_name(name):
             return

         if not self.common_function.check_price(price):
             return

         if len(str(barcode)) == 10 and int(cnt) > 0 and int(price) > 0 and (
                 event == '1+1' or event == '2+1' or event == '') and (limit == '구매가능' or limit == '구매불가'):
             if limit == '구매가능':
                 limit = 0
             else:
                 limit = 1

             if event == '':
                 event = 'null'
             else:
                 event = '"' + event + '"'
             check = True

         if check:
             stock_manager.product_info_modification(str(self.__last_barcode) ,str(barcode), name, str(cnt), str(price), event, str(limit))
             self.common_function.msg_box('수정되었습니다.\n수정을 완료했으면 창을 닫으십시오.     ')
         else:
             self.common_function.msg_box(
                 '--------------------------------------------\nInput Error : 입력이 올바르지 않습니다.   \n--------------------------------------------\n바코드 : 10자리\n행사 : "1+1" or "2+1" or ""\n미성년자 : "구매가능" or "구매불가"')

    def delete_clicked(self):
        '''
        초기화면으로 리셋함
        :param self:
        :return:
        '''
        self.lbarcode.setText("")
        self.lgoodsname.setText("")
        self.lgoodscnt.setText("")
        self.lgoodsprice.setText("")
        self.ltotal.setText("")
        self.lgoodsevent.setText("")
        self.lgoodslimit.setText("")
