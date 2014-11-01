#encoding=utf-8
import urllib
import urllib2
import re
import MySQLdb
import login
import crawle_page

post_counter = 0
page = 0

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

    login.login()

    url = "http://bbs.hackbase.com/forum.php?mod=forumdisplay&fid=397"    

    page_url = url
    html = urllib2.urlopen(page_url).read().decode('gbk').encode('utf8')
    tem_page = 0
    if self.page != 0:
        page_url = url + "&page=" + str(page)
        tem_page = 1

    else:
        self.page =1
        page_url = url
    while page < 6:
        crawle_page.get_page(page_url)
        page += 1
        page_url = url + "&page=" + str(page)
