from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models

# Create your models here.


def register(title, content):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        insert
          into board
        values (null,
                %s,
                %s,
                0,
                now(),
                ifnull((select max(g_no) from board a), 0) + 1,
                1,
                1,
                1);
    '''
    cursor.execute(sql, (title, content))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def fetchone(email, password):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no, name, email, password
          from user
         where email=%s
           and password=password(%s)

    '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

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

