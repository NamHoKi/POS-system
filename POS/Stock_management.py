from DB_helper import DB_helper

class Stock_management(object):
    def product_input(self, num, name, quan, price, event, minor):
        '''
        DB에 Product를 추가하는 sql을 생성해서 DB_helper로 보냄
        :param num: string - 바코드
        :param name: string - 이름
        :param quan: string - 수량
        :param price: string - 가격
        :param event: string - 이벤트
        :param minor: string - 미성년자구매
        :return:
        '''
        helper = DB_helper()
        sql = 'insert into product values (' + num + ', ' + '"'+ name + '"' + ', ' + quan + ', ' + price +', ' + event +  ', ' + minor + ')' + ';'
        helper.execute(sql)

    def product_delete(self, num):
        '''
        DB에 Product를 삭제하는 sql을 생성해서 DB_helper로 보냄
        :param num: string - 바코드
        :return:
        '''
        helper = DB_helper()
        sql = 'delete from product where num = ' + num + ';'
        helper.execute(sql)

    def product_check(self):
        '''
        DB에 Product를 모두 조회하는 sql을 생성해서 DB_helper로 보냄
        :return: list - 재고 리스트
        '''
        helper = DB_helper()
        sql = 'select * from product' + ';'
        return helper.db_return_list(sql)

    def product_quan_modification(self, num, quan):
        '''
        DB에 Product의 수량을 수정하는 sql을 생성해서 DB_helper로 보냄
        :param num: string - 수정할 제품의 바코드
        :param quan: string - 수정할 제품의 수량
        :return:
        '''
        helper = DB_helper()
        sql = 'UPDATE PRODUCT SET quantity = ' + str(quan) + ' WHERE pro_num = ' + str(num) + ';'
        helper.execute(sql)

    def product_search(self, barcode):
        '''
        DB에 Product를 검색하는 sql을 생성해서 DB_helper로 보냄
        :param barcode: string - 바코드
        :return: list - 검색한 제품 정보
        '''
        helper = DB_helper()
        sql = 'select * from product where pro_num = ' + str(barcode) + ';'
        pro = helper.db_return(sql)
        return pro

    def product_info_modification(self, col, num, name, quan, price,event, minor):
        '''
        DB에 Product의 수량을 수정하는 sql을 생성해서 DB_helper로 보냄
        :param col: string - 수정 할 제품의 바코드
        :param num: string - 수정 될 바코드
        :param name: string - 수정 될 이름
        :param quan: string - 수정 될 수량
        :param price: string - 수정 될 가격
        :param event: string - 수정 될 이벤트
        :param minor: string - 수정될 미성년자구매
        :return:
        '''
        helper = DB_helper()
        sql = 'UPDATE PRODUCT SET pro_num = ' + num + ', pro_name = ' + '"' + name + '"' + ', quantity = ' + quan + ', price = ' + price + ', event_type = ' + event + ', minor = ' + minor + ' WHERE pro_num = ' + col + ';'
        helper.execute(sql)

    def product_event_list(self):
        '''
        DB에 Product의 event_type이 '1+1' 이거나 '2+1'인 제품을 조회하는 sql을 만들어서 DB_helper로 보냄
        :return: list - 행사상품인 재고 리스트
        '''
        helper = DB_helper()
        sql = 'select * from product where event_type = "1+1" or event_type = "2+1"'
        list = helper.db_return_list(sql)
        return list