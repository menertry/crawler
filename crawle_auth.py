import urllib
import urllib2
import re

def get_id(html)
    reg = r'UID[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][5:-8]
    return str_id

def get_name(html)
    reg = r'spacename"[\s\S]+?</strong>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    name = imglist[0][25:-24]
    return name

def get_tim_jdate_vl_rp_my(html)
    reg = r'<li><em>[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    time = imglist[5][25:-5]
    join_date = imglist[6][25:-5]
    value = imglist[12][19:-5]
    reputation = imglist[13][19:-5]
    money = imglist[14][19:-5]
    return [time, join_date, value, reputation, money]

def get_level(html)#!!!!!!!
    reg = r'gid=[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    level = imglist[0][4:-1]
    return level

def get_post_num(html)
    reg = r'type=reply[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    post_num = imglist[0][49:-4]
    return post_num

def get_topic_num(html)
    reg = r'type=thread[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    topic_num = imglist[0][50:-4]
    return topic_num

def get_auth(url)
    html = urllib2.urlopen(url).read()
    html_utf8 = html.decode('gbk').encode('utf8')

    auth_id = get_id(html_utf8)
    name = get_name(html_utf8)
    au_list = get_tim_jdate_vl_rp_my(html_utf8)
    level = get_level(html_utf8)
    post_num = get_post_num(html_utf8)
    topic_num = get_topic_num(html_utf8)
    return [auth_id, name, au_list[0], au_list[1], au_list[2], au_list[3], au_list[4], level, post_num, topic_num] 
