from DB_helper import DB_helper


class Payment_manage(object):

    def check_sales_product_real_day(self, year, month, day):
        '''
        해당 날짜의 결제된 제품 리스트를 리턴함
        :param year: string - 년
        :param month: string - 월
        :param day: string - 일
        :return: list - 결제된 제품 리스트
        '''
        pay_nums = self.check_sales_return_paynum_day(year, month, day)

        helper = DB_helper()
        total_list = []
        for num in pay_nums:
            sql = 'select * from payment_detail where pay_num = ' + str(num)
            detail = helper.db_return_list(sql)
            total_list.append(detail)

        return total_list

    def check_sales_product_real_month(self, year, month):
        '''
        해당 월의 결제된 제품 리스트를 리턴함
        :param year: string - 년
        :param month: string - 월
        :return: list - 결제된 제품 리스트
        '''
        pay_nums = self.check_sales_return_paynum_month(year, month)

        helper = DB_helper()
        total_list = []
        for num in pay_nums:
            sql = 'select * from payment_detail where pay_num = ' + str(num)
            detail = helper.db_return_list(sql)
            total_list.append(detail)

        return total_list

    def check_sales_product_real_year(self, year):
        '''
        해당 년의 결제된 제품 리스트를 리턴함
        :param year: string - 년
        :return: list - 결제된 제품 리스트
        '''
        pay_nums = self.check_sales_return_paynum_year(year)

        helper = DB_helper()
        total_list = []
        for num in pay_nums:
            sql = 'select * from payment_detail where pay_num = ' + str(num)
            detail = helper.db_return_list(sql)
            total_list.append(detail)

        return total_list

    def check_sales_year_return_paylist(self, year):
        '''
        해당 년의 결제 내역을 리턴함
        :param year: string - 년
        :return: list - 결제 내역 리스트
        '''
        numbers = self.check_sales_return_paynum_year(year)

        helper = DB_helper()
        real_paylist = []
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num)
            paylist = helper.db_return_list(sql)
            for i in paylist:
                i[1] = i[1].strftime('%Y-%m-%d %H:%M:%S')
            real_paylist.append(paylist)

        return real_paylist

    def check_sales_month_return_paylist(self, year, month):
        '''
        해당 연월의 결제 내역을 리턴
        :param year: string - 년
        :param month: string - 월
        :return: list - 결제 내역 리스트
        '''
        numbers = self.check_sales_return_paynum_month(year, month)

        helper = DB_helper()
        real_paylist = []
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num)
            paylist = helper.db_return_list(sql)
            for i in paylist:
                i[1] = i[1].strftime('%Y-%m-%d %H:%M:%S')
            real_paylist.append(paylist)

        return real_paylist

    def check_sales_day_return_paylist(self, year, month, day):
        '''
        해당 날짜의 결제 내역을 리턴
        :param year: string - 년
        :param month: string - 월
        :param day: string - 일
        :return: list - 결제 내역 리스트
        '''
        numbers = self.check_sales_return_paynum_day(year, month, day)

        helper = DB_helper()
        real_paylist = []
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num)
            paylist = helper.db_return_list(sql)
            for i in paylist:
                i[1] = i[1].strftime('%Y-%m-%d %H:%M:%S')
            real_paylist.append(paylist)

        return real_paylist

    def check_sales_return_paynum_day(self, year, month, day):
        '''
        해당 날짜의 결제내역 번호를 리턴
        :param year: string - 연
        :param month: string - 월
        :param day: string - 일
        :return: list - 결제내역 번호 리스트
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment'
        day_list = helper.db_return_list(sql)
        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == int(year) and daytuple.tm_mon == int(month) and daytuple.tm_mday == int(day):
                numbers.append(tu[0])

        return numbers

    def check_sales_return_paynum_month(self, year, month):
        '''
        해당 연월의 결제 내역 번호를 리턴
        :param year: string - 연
        :param month: string - 월
        :return: list - 결제내역 번호 리스트
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == int(year) and daytuple.tm_mon == int(month):
                numbers.append(tu[0])

        return numbers

    def check_sales_return_paynum_year(self, year):
        '''
        해당 연의 결제내역 번호 리스트를 리턴
        :param year: string - 연
        :return: list - 결제내역 번호 리스트
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == int(year):
                numbers.append(tu[0])

        return numbers

    def check_sales_method(self, method):
        '''
        결제수단에 해당하는 매출액을 리턴
        :param method: string - 결제수단(현금 or 카드 or 상품권)
        :return: int - 매출액
        '''
        helper = DB_helper()
        sql = 'select num, method from payment'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tu_method = tu[1]
            if tu_method == method:
                numbers.append(tu[0])

        total_money = 0
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num)
            paylist = helper.db_return_list(sql)
            for i in paylist:
                total_money += i[4]

        return total_money

    def check_sales_year(self, year):
        '''
        해당 년의 매출액을 리턴
        :param year: string - 연
        :return: int - 매출액
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment;'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == year:
                numbers.append(tu[0])

        total_money = 0
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num) + ';'
            paylist = helper.db_return_list(sql)
            for i in paylist:
                total_money += i[4]

        return total_money

    def check_sales_month(self, year, month):
        '''
        해당 연월의 매출액을 리턴
        :param year: string - 연
        :param month: string - 월
        :return: int - 매출액
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment;'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == year and daytuple.tm_mon == month:
                numbers.append(tu[0])

        total_money = 0
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num) + ';'
            paylist = helper.db_return_list(sql)
            for i in paylist:
                total_money += i[4]

        return total_money

    def check_sales_today(self, year, month, day):
        '''
        해당 날짜의 매출액을 리턴
        :param year: string - 연
        :param month: string - 월
        :param day: string - 일
        :return: int - 매출액
        '''
        helper = DB_helper()
        sql = 'select num, paytime from payment;'
        day_list = helper.db_return_list(sql)

        numbers = []
        for tu in day_list:
            tday = tu[1]
            daytuple = tday.timetuple()
            if daytuple.tm_year == year and daytuple.tm_mon == month and daytuple.tm_mday == day:
                numbers.append(tu[0])

        total_money = 0
        for num in numbers:
            sql = 'select * from payment where num = ' + str(num) + ';'
            paylist = helper.db_return_list(sql)
            for i in paylist:
                i[1] = i[1].strftime('%Y-%m-%d %H:%M:%S')
                total_money += i[4]

        return total_money

    def remove_payment(self, number):
        '''
        영수증 번호에 해당하는 결제내역을 payment 테이블에서 삭제
        :param number: string - 영수증번호
        :return:
        '''
        helper = DB_helper()
        sql = 'delete from payment where num = ' + number + ';'
        helper.execute(sql)

    def remove_payment_detail(self, pay_num):
        '''
        영수증 번호에 해당하는 결제된 제품 내역을 payment_detail 테이블에서 삭제
        :param pay_num: string - 영수증 번호
        :return:
        '''
        helper = DB_helper()
        sql = 'delete from payment_detail where pay_num = ' + pay_num + ';'
        helper.execute(sql)

    def return_detail(self, number):
        '''
        영수증 번호에 해당하는 결제된 제품 내역을 리턴
        :param number: string - 영수증 번호
        :return: list - 결제된 제품 내역
        '''
        helper = DB_helper()
        sql = 'select * from PAYMENT_DETAIL where pay_num = ' + str(number) + ';'
        return helper.db_return_list(sql)

    def check_payment(self):
        '''
        payment 테이블에서 전체 결제 내역 리스트를 조회
        :return: list - 결제내역
        '''
        helper = DB_helper()
        sql = 'select * from payment'
        list = helper.db_return_list(sql)
        return list

    def check_payment_number(self, paynum):
        '''
        영수증 번호에 해당하는 결제 내역을 리턴
        :param paynum: string - 영수증 번호
        :return: list - 결제내역
        '''
        helper = DB_helper()
        sql = 'select * from payment where num = ' + paynum + ';'
        list = helper.db_return_list(sql)
        return list

    def check_barcode(self, paynum):
        '''
        영수증 번호에 해당하는 결제 내역을 리턴
        :param paynum: string - 영수증 번호
        :return: list - 결제내역
        '''
        helper = DB_helper()
        sql = 'select * from payment where num = ' + paynum + ';'
        list = helper.db_return(sql)
        return list