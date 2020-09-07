from django.shortcuts import render
import user.models as usermodels
from MySQLdb import connect
from MySQLdb.cursors import DictCursor


def fetchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select name, email, gender
          from user
         where no=%s

    '''

    cursor.execute(sql, no)
    result = cursor.fetchonebyno()

    # 자원 정리
    cursor.close()
    conn.close()

    return result


def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.53',
        port=3306,
        db='mysite',
        charset='utf8')

fetchonebyno(1)