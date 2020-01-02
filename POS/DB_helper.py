import pymysql

class DB_helper(object):
    def execute(self, sql):
        '''
        DB에 직접적으로 접속하고 sql문을 수행하는 함수
        :param sql: string - SQL문
        :return:
        '''
        conn = pymysql.connect(host='210.125.112.219', user='scott', password='tiger', db='pos', charset='utf8')
        try:
            with conn.cursor() as curs:
                curs.execute(sql)
                conn.commit()
        finally:
            conn.close()

    def db_return(self, sql):
        '''
        self.execute()에 접속해서 받아온 값을 반환하는 함수
        :param sql: string - SQL문
        :return: string or list - 질의결과
        '''
        conn = pymysql.connect(host='210.125.112.219', user='scott', password='tiger', db='pos', charset='utf8')
        rows = None
        try:
            with conn.cursor() as curs:
                curs.execute(sql)
                rows = curs.fetchall()
                rows = list(rows)
                for i in range(len(rows)):
                    rows[i] = list(rows[i])
        finally:
            conn.close()
            return rows[0]

    def db_return_list(self, sql):
        '''
        self.execute()에 접속해서 받아온 값을 반환하는 함수
        :param sql: string - SQL문
        :return: list - 질의결과
        '''
        conn = pymysql.connect(host='210.125.112.219', user='scott', password='tiger', db='pos', charset='utf8')
        rows = None
        try:
            with conn.cursor() as curs:
                curs.execute(sql)
                rows = curs.fetchall()
                rows = list(rows)
                for i in range(len(rows)):
                    rows[i] = list(rows[i])
        finally:
            conn.close()
            return rows
