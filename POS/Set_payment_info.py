from DB_helper import DB_helper
from datetime import datetime as dt

class Set_payment_info(object):
    def set_payment_number(self):
        '''
        DB에 Payment의 num 값중 가장 큰 값을 반환하는 sql을 생성해서 DB_helper로 보냄
        :return: int - 새로운 영수증 바코드
        '''
        helper = DB_helper()
        sql = 'select max(num) from PAYMENT'
        max = helper.db_return(sql)
        if max[0] == None:
            payment_number = 7000000
        else:
            payment_number = int(max[0]) + 1

        return payment_number

    def send_payment_detail(self,pro_list, payment_number):
        '''
        DB에 Payment_detail의 투플을 추가하는는 sql을 생성해서 DB_helper로 보냄
        :param pro_list: string - 제품 바코드
        :param payment_number: string - 영수증 바코드
        :return:
        '''
        helper = DB_helper()
        for pd in pro_list:     #pd는 제품번호, 이름, 원래가격, 수량, 총가격, 이벤트 순서
            if pd[5] == None:
                pd[5] = 'null'
                sql = 'insert into PAYMENT_DETAIL(pro_num, pro_name, original_price, quantity, total_price, event_type, pay_num) ' + 'values(' + str(
                    pd[0]) + ', \'' + str(pd[1]) + '\', ' + str(pd[2]) + ', ' + str(pd[3]) + ', ' + str(
                    pd[4]) + ', ' + str(pd[5]) + ', ' + str(payment_number) + ');'
            else:
                sql = 'insert into PAYMENT_DETAIL(pro_num, pro_name, original_price, quantity, total_price, pay_num) ' + 'values(' + str(pd[0]) + ', \'' + str(pd[1]) + '\', ' + str(pd[2]) + ', ' + str(pd[3]) +', '+ str(pd[4]) + ', '+ str(payment_number) + ');'
            helper.execute(sql)

    def send_payment_result(self,payment_number, now, method, method_info, total_price):
        '''
        DB에 Payment의 투플을 추가하는 sql을 생성해서 DB_helper로 보냄
        :param payment_number: string - 영수증 번호
        :param now: string - 결제 시각
        :param method: string - 결제 수단
        :param method_info: string - 결제 수단 정보
        :param total_price: string - 총 금액
        :return:
        '''
        helper = DB_helper()
        sql = 'insert into PAYMENT values(' + str(payment_number)  + ', \'' + now + '\', ' + '\'' + str(method) +'\', \'' + str(method_info) + '\', ' + str(total_price) + ');'
        helper.execute(sql)

    def read_datetime(self):
        '''
        현재 시각을 string type으로 리턴함
        :return: string - 현재 시각
        '''
        now = str(dt.now())
        return now