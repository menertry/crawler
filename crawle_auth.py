import urllib
import urllib2
import re

html = urllib2.urlopen("LINKING")
html_utf8 = html.decode('gbk').encode('utf8')

get_id(html_utf8)
get_name(html_utf8)
get_tim_jdate_vl_rp_my(html_utf8)
get_level(html_utf8)
get_post_num(html_utf8)
get_topic_num(html_utf8)

def get_id(html)
    reg = r'UID[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][5:-8]

def get_name(html)
    reg = r'spacename"[\s\S]+?</strong>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_name = imglist[0][25:-24]

def get_tim_jdate_vl_my(html)
    reg = r'<li><em>[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_time = imglist[5][25:-5]
    str_join_date = imglist[6][25:-5]
    str_value = imglist[12][19:-5]
    str_reputation = imglist[13][19:-5]
    str_money = imglist[14][19:-5]

def get_level(html)
    reg = r'gid=[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_level = imglist[0][4:-1]

def get_post_num(html)
    reg = r'type=reply[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_post_num = imglist[0][49:-4]

def get_topic_num(html)
    reg = r'type=thread[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_topic_num = imglist[0][50:-4]
