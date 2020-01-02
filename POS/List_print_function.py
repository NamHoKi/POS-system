from Common_function import Common_function

class List_print_function(Common_function):
    def number_print(self, number):
        l = len(number)
        number = number + ' '*(10 - l)
        return number

    def name_print(self, name):
        l = 0
        for token in str(name):
            if (ord(token) >= 48 and ord(token) <= 57) or (ord(token) >= 65 and ord(token) <= 90) or (ord(token) >= 97 and ord(token) <= 112):
                l += 1
            else:
                l += 2
        name = ' ' * (18 - (l)) + name + ' ' * 7
        return name

    def minor_print(self,minor):
        if minor == '1':
            minor = '구매불가'
        else:
            minor = '구매가능'
        text = minor + ' ' * 8
        return text

    def price_print(self, price):
        price = super().insert_comma(price)
        l = len(price)
        price = ' ' * (11 - l) + price + ' ' * 6
        return price

    def count_print(self, count):
        count = str(count)
        l = len(count)
        count = ' ' * (5 - l) + count + ' ' * 7
        return count

    def event_print(self, event):
        if event != '1+1' and event != '2+1':
            return ' '
        return event

    def detail_pay_return_in_payment_mode(self, pay_list):
        buf = ''

        for info in pay_list:
            for i in range(len(info)):
                if i == 0:
                    buf += ' ' * 9 + str(info[i])
                elif i == 1:
                    buf += ' ' * 17 + str(info[i])
                elif i == 2:
                    if info[i] == '상품권':
                        buf += ' ' * 11 + str(info[i])
                    else:
                        buf += ' ' * 13 + str(info[i])
                elif i == 3:
                    if info[2] == '현금':
                        buf += ' ' * 20 + '-' + ' ' * 13
                    elif info[2] == '카드':
                        buf += ' ' * 12 + str(info[i]) + ' ' * 6
                    else:
                        buf += ' ' * 10 + str(info[i]) + ' ' * 4
                else:
                    common_function = Common_function()
                    buf += str(common_function.insert_comma(info[i]))
            buf += '\n'
        return buf