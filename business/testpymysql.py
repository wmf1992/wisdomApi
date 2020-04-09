import pymysql.cursors
import json
connection = pymysql.connect(host='10.0.100.88',
                             user='yxsoft',
                             password='yxsoft',
                             db='yxsoft',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `uid`, `nickname` FROM `house_user`"
        cursor.execute(sql)
        result = cursor.fetchone()      # 获取第一行
        resultall = cursor.fetchall()   # 获取所有
        print(resultall)
finally:
    connection.close()