# coding=utf-8
# Time   : 2019/6/27 9:43
# Author : zhonglin.zhang
# File   : dbutil.py

import allure
import pymysql


class DbUtil:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def get_connection(self):
        connection = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                     password=self.password, db=self.db, charset="utf8")

        return connection

    def get_cursor(self):
        cursor = self.get_connection().cursor(pymysql.cursors.DictCursor)
        return cursor

    @allure.step("执行sql语句")
    def query(self, sql):
        """
        查询结果只有一条记录
        :param sql:
        :return: dict
        """
        cursor = self.get_cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    @allure.step("执行sql语句")
    def query_all(self, sql):
        """
        查询结果有多条记录
        :param sql:
        :return: list
        """
        cursor = self.get_cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    db_ = DbUtil("localhost", 3306, "root", "Eylaine@1989", "test")
    result_ = db_.query("select * from demo")
    print(result_["id"])
