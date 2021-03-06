#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base.base import connection
class SubProjectDb:
    # 查找最新的一条待录入数据的记录
    def sub_project_list(self,statu):
        try:
            # with connection.cursor() as cursor:
            #     # Create a new record
            #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
            #
            # connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT MAX(id) FROM wisdom_project_settlement WHERE STATUS=%d" %statu
                cursor.execute(sql)
                result = cursor.fetchone()      # 获取第一行
                # print(result['MAX(id)'])
                return result['MAX(id)']
        finally:
            pass
            # connection.close()