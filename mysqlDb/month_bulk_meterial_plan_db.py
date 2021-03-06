from base.base import connection
class MonthBulkMeterialPlanDb:
    # 查找最新的一条待录入数据的记录
    def month_bulk_meterial_list(self,statu):
        try:
            # with connection.cursor() as cursor:
            #     # Create a new record
            #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
            #
            # connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT MAX(id) FROM wisdom_month_bulk_meterial_plan WHERE STATUS=%d" %statu
                cursor.execute(sql)
                result = cursor.fetchone()      # 获取第一行
                # print(result['MAX(id)'])
                return result['MAX(id)']
        finally:
            pass
            # connection.close()