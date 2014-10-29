import urllib
import urllib2
import re

def get_url(html)
    reg = r'regex'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for url in imglist 
        imglist[counter] = url[]
    return imglist

def if_end(html)
    reg = r'regex'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    return 1

def get_page(url, curosr)
    html = urllib2.urlopen(url).read()
    html_utf8 = html.decode('gbk').encode('utf8')
    url_list = get_url(html_utf8)
    for url in url_list
        get_post(url, cursor)
    return if_end(html_utf8)
