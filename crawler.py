#encoding=utf-8
import urllib
import urllib2
import re
import chardet
import login
from post import Post
from tid_getter import Tid_getter
import threading
import MySQLdb
import pdb
    
post = 0
floor = 0
auth_set = {}

def post_finish():
    global post
    post += 1
    print 'finish '+str(post)+' post, '+str(floor)+' floor'

def floor_finish():
    global floor
    floor += 1
    print 'finish '+str(post)+' post, '+str(floor)+' floor'
    
def insert(sql):
    db = MySQLdb.connect("localhost","root","","mysql",charset="utf8")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except:
#        print sql
        pass
    finally:
        db.commit()
        db.close()

def replace(string, be_replaced, replace):
    index = string.find(be_replaced)
    while index != -1:
        string = string[0:index] + replace + string[index+len(be_replaced):]
        index = string.find(be_replaced)
    return string

def get_a_post():
    return urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid=2831312&extra=page%3D2')
    
def regex(reg, html):
    imgre = re.compile(reg)
    return re.findall(imgre, html)
    
def lable_cut(string):
    reg = r'<[\s\S]+?>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, string)
    for cut in imglist:
        index = string.find(cut)
        string = string[0:index]+string[index+len(cut):]
    return string

def urlopen(url):
    try:
        html = urllib2.urlopen(url).read()
        encode_dict = chardet.detect(html)
        if encode_dict['encoding'] == 'UFT-8' or encode_dict['encoding'] == 'utf-8':
            html = html
        else:
            html = html.decode('gbk','ignore').encode('utf8')
        return html
    except:
        return urlopen(url)
   
def get_start():
    url = 'http://bbs.hackbase.com/forum.php?mod=forumdisplay&fid=378'
    total_thread = 25
    login.login()
    thread_list = []
    queue = []
    tid_getter = Tid_getter(url)
    post_getter = []
    i = 0
    print 'Begin multithread'
    while i < total_thread:
        post_getter.append(Post(tid_getter.tid_list))
        thread_list.append(threading.Thread(target = post_getter[i].crawle))
        thread_list[i].start()
        i += 1
    print 'Begin get tid'
    tid_getter.crawle()
    
    i = 0
    while i<total_thread:
        thread_list[i].join()
        i += 1
