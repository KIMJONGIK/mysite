from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def register(title, content, no):
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
                %s);
    '''
    cursor.execute(sql, [title, content, (no,)])
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def fetchlist(page):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    pages = (int(page)-1)*5

    sql = '''
        select b.no,
            b.title,
            b.content,
            b.hit,
            b.reg_date,
            b.g_no,
            b.o_no,
            b.depth,
            b.user_no,
            u.name,
            u.no
          from board as b, user as u
          where b.user_no = u.no
          order by g_no desc, o_no asc 
           limit %s, 5
    '''
    cursor.execute(sql, (pages,))
    result = cursor.fetchall()

    # 자원 정리
    cursor.close()
    conn.close()

    return result


def fetchone(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select b.no as board_no, b.title, b.content, u.no as user_no
        from board as b, user as u
        where b.user_no = u.no
        and b.no=%s
    '''
    cursor.execute(sql, no)
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result


def delete(no):
    conn = getconnection()
    cursor = conn.cursor()

    sql = 'delete from board where no=%s'
    cursor.execute(sql, [no])
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def hit(no):
    conn = getconnection()
    cursor = conn.cursor()

    sql = 'update board set hit=hit+1 where no=%s'
    cursor.execute(sql, (no,))
    conn.commit()

    cursor.close()
    conn.close()


def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.53',
        port=3306,
        db='mysite',
        charset='utf8')

