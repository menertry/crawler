import urllib
import urllib2
import re

def get_id(html)
    reg = r'UID[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][5:-8]
    id = string.atoi(str_id)
    return id

def get_name(html)
    reg = r'spacename"[\s\S]+?</strong>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_name = imglist[0][25:-24]
    return name

def get_tim_jdate_vl_my(html)
    reg = r'<li><em>[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_time = imglist[5][25:-5]
    str_join_date = imglist[6][25:-5]
    str_value = imglist[12][19:-5]
    str_reputation = imglist[13][19:-5]
    str_money = imglist[14][19:-5]
    return [time, join_date, value, reputation, money]

def get_level(html)
    reg = r'gid=[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_level = imglist[0][4:-1]
    level = string.atoi(str_level)
    return level

def get_post_num(html)
    reg = r'type=reply[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_post_num = imglist[0][49:-4]
    post_num = string.atoi(str_post_num)
    return post_num

def get_topic_num(html)
    reg = r'type=thread[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_topic_num = imglist[0][50:-4]
    topic_num = string.atoi(str_topic_num)
    return topic_num

def get_auth(url, id, floor, date,  content)
    html = urllib2.urlopen(url)
    html_utf8 = html.decode('gbk').encode('utf8')

    auth_id = get_id(html_utf8)
    name = get_name(html_utf8)
    list = get_tim_jdate_vl_rp_my(html_utf8)
    level = get_level(html_utf8)
    post_num = get_post_num(html_utf8)
    topic_num = get_topic_num(html_utf8)
    sql = "".join("insert into post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_join_date,auth_post_num,auth_topic_num,auth_time,auth_level,auth_money,auth_reputation,auth_value)values(",id,floor,date,content,auth_id,name,list[1],post_num,topic_num,list[0],level,list[4],list[3],list[2],");"
     cursor.execute(sql)
