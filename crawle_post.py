import urllib
import urllib2
import re

html = urllib2.urlopen('LINKING')
html_utf8 = html.decode('gbk').encode('utf8')

get_title(html_utf8)
get_content(html_utf8)
get_view_reply(html_utf8)
get_id_date(html_utf8)

get_auth_links(html_utf8)

get_post_detail(links,content,floor,date)

def get_title(html)
    reg = r'<span id="thread_subject">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_title = imglist[0][26:-7]

def get_content(html)
    reg = r'<div style="height:2px; overflow:hidden;">[\s\S]+?</div>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

def get_id_date(html)
    reg = r'<em id="authorposton[\s\S]+?</em>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][20:-35]
    str_date = imglist[0][-23:-5]

def get_view_reply(html)
    reg = r'<span class="xi1">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_view = imglist[0][24:-13]
    str_reply = imglist[1][24:-13]

def get_auth_links
