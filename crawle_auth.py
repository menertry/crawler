import urllib
import urllib2
import re

def get_join_date(html)
    reg = r'注册时间<[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist[0][17:-5]

def get_reputation(html)
    reg = r'威望<[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist[0][11:-6]

def get_money(html)
    reg = r'黑币<[\s\S]+?</li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist[0][11:-6]

def get_auth(url)
    html = urllib2.urlopen(url).read().decode('gbk').encode('utf8')

    join_date = get_join_date(html)
    reputation = get_reputation(html)
    money = get_money(html)

    return [join_date, reputation, money]
