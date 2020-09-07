from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def insert(name, email, password, gender):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        insert
          into user
        values (null, %s, %s, password(%s), %s, now())
    '''
    cursor.execute(sql, (name, email, password, gender))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def fetchone(email, password):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select email, password
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


def fatchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no, name, email, gender
          from user
         where no=%s

    '''
    cursor.execute(sql)
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