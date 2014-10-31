#encoding=utf-8
import urllib
import urllib2
import re
import MySQLdb
import login
import crawle_page

post_counter = 0

def insert(sql):
    db = MySQLdb.connect("localhost","root","","mysql",charset="utf8")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    finally:
        db.commit()
        db.close()


def replace(string, be_replaced, replace):
    index = string.find(be_replaced)
    while index != -1:
        string = string[0:index] + replace + string[index+len(be_replaced):]
        index = string.find(be_replaced)
    return string

def crawle():

#    sql = """insert into main_post(post_id,post_title,post_view,post_reply,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values(123,"123",123,123,"123","123",123,"123","123","123",123,123,123,123,123,123);"""

    login.login()

    url = "http://bbs.hackbase.com/forum.php?mod=forumdisplay&fid=397"    

    page_url = url
    html = urllib2.urlopen(page_url).read().decode('gbk').encode('utf8')
    page = 1

    while crawle_page.get_page(page_url) != 1:
        page += 1
        page_url = url + "&page=" + string.itoa(page)
