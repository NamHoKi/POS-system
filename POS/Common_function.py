from PyQt5.QtWidgets import QMessageBox

class Common_function(object):
    def msg_box(self, text):
        '''
        메시지 박스에 text를 띄워서 출력함
        :param text: string - 전달할 메시지
        :return:
        '''
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec()

    def insert_comma(self, money):
        '''
        가격을 쉽게 구분하기 위해 ,를 넣음
        :param money: string - ,를 삽입할 금액
        :return: string - ,를 삽입한 금액
        ex) money = '1000'    -> return : '1,000'
            money = '1000000' -> return : '1,000,000'
            money = '100'     -> return : '100'
        '''
        money = str(money)
        cnt = 0
        result = ''
        for i in range(1, len(money) + 1):
            if cnt == 3:
                cnt = 0
                result = ',' + result
            result = money[-1 * i] + result
            cnt += 1

        return result

    def text_write(self,file_name,text):
        '''
        파일에 text를 씀
        :param file_name: string - 파일 경로
        :param text: string - 내용
        :return:
        '''
        with open(file_name,'w',encoding='utf-8') as f:
            f.write(str(text))

    def text_read(self,file_name):
        '''
        파일의 text를 리턴함
        :param file_name: 파일 경로
        :return: 파일 내용
        '''
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
        return text

    def receipt_print_form(self,date,detail,receipt_num):
        '''
        기본적인 영수증 틀에 매개변수들을 넣어서 영수증을 만들어서 메모장으로 출력함(메모장 실행)
        :param date: string - 날짜
        :param detail: string - 결제 내역
        :param receipt_num: string - 영수증 번호
        :return:
        '''
        buf = 'SW부경대점              051-123-4567\n'
        buf += '최선한                    2815600151\n'
        buf += '부산 남구 용소로 45 향파관(A15)302호\n'
        buf += str(date) + ' 전*현    NO:21908\n'
        buf += '-----------------------------------------\n'
        buf += '*정부방침에 의해 교환/환불은\n'
        buf += '반드시 영수증을 지참하셔야 합니다.\n'
        buf += '-----------------------------------------\n'

        for token in detail:
            buf += str(token[0]) + ' ' * (10 - len(str(token[0]))) + str(token[1]) + ' ' * (
                        10 - len(str(token[1]))) + self.insert_comma(token[5]) + '\n'
        buf += '-----------------------------------------\n'
        buf += '영수증 번호 : ' + str(receipt_num)

        self.text_write('text/receipt.txt',buf)

        import os
        path = str(os.path.abspath('./text/receipt.txt'))
        os.system(path)

    def check_barcode(self,barcode):
        '''
        바코드의 조건을 체크함
        :param barcode:
        :return:
        '''
        for token in barcode:
            if not (48 <= ord(token) and ord(token) <= 57):
                self.msg_box('바코드는 숫자 10자리만 가능합니다.     ')
                return False
        return True

    def check_name(self,name):
        '''
        상품의 이름이 될 조건을 체크하고 True or False를 리턴함
        :param name: string - 상품이름
        :return: bool - True : 조건 만족 // False : 조건 불만족
        '''
        for token in name:
            if (ord(token) >= 48 and ord(token) <= 57) or (ord(token) >= 65 and ord(token) <= 90) or (
                    ord(token) >= 97 and ord(token) <= 112) or (ord(token) >= 44032 and ord(token) <= 55203):
                pass
            else:
                self.msg_box('상품이름이 올바르지 않습니다.      ')
                return False
        return True

    def check_price(self,price):
        '''
        상품의 가격이 될 조건을 체크하고 True or False를 리턴함
        :param name: string - 상품가격
        :return: bool - True : 조건 만족 // False : 조건 불만족
        '''
        for token in price:
            if not (48 <= ord(token) and ord(token) <= 57):
                self.msg_box('단가와 수량은 숫자만 입력가능합니다.     ')
                return False
        return True

    def check_number(self,number):
        '''
        숫자만으로 된 문자열인지 체크함
        :param number: string - 확인할 숫자 문자열
        :return: bool - Ture : 조건 만족 // False : 조건 불만족
        '''
        for token in number:
            if not (48 <= ord(token) and ord(token) <= 57):
                self.msg_box('숫자만 입력하시오.     ')
                return False
        return True

    def event_processing(self, list_buf, index):
        '''
        할인 금액을 계산해서 리턴함
        :param list_buf: list - 결제 상품 리스트
        :param index: int - list_buf 의 index
        :return: int - 할인 금액
        '''
        # self.list_buf : [barcode, name, int(price), count, int(price) * count, event]
        price = int(list_buf[index][2])
        count = int(list_buf[index][3])
        event = list_buf[index][5]
        return self.event_processing_return(event,count,price)

    def event_processing_return(self,event,count,price):
        if event == '1+1':
            return int(count / 2) * int(price)
        elif event == '2+1':
            return int(count / 3) * int(price)
        else:
            return 0

    def modify_list_buf(self,list_buf):
        '''
        list_buf를 최신화 함
        :param list_buf: list - 결제 리스트
        :return: list - 결제 리스트
        '''
        total_money, discount, result, get_money, rest_money = 0, 0, 0, 0, 0
        index = 0
        for i in range(len(list_buf)):
            total_money = int(list_buf[i][4])
            discount = self.event_processing(list_buf,index)
            list_buf[i][4] = total_money - discount
            index += 1
        return list_buf

    def result_print(self,list_buf):
        '''
        계산에 필요한 값들을 계산하고 리턴
        :return: list - [총 금액, 할인 금액, 계산 금액, 받은 금액, 거스름 돈]
        '''
        total_money, discount, result, get_money, rest_money = 0, 0, 0, 0, 0

        index = 0
        for i in list_buf:
            total_money += int(i[4])                              #total_money 계산
            discount += self.event_processing(list_buf, index)    # 할인된 금액 계산
            result = total_money - discount
            index += 1

        return [total_money,discount,result,get_money,rest_money]