import urllib
import urllib2
import re

def get_url(html)
    reg = r'previewThread[\s\S]+?onclick'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for url in imglist 
        string = url
        index = string.find("viewthread")
        string = string[index:-9]
        imglist[counter] = string
        counter += 1
    return imglist

def if_end(html)
    if current_page(html) == total_page(html)
        return 1
    else
        return 0

def current_page(html)
    reg = r'curpage="[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(reg, html)
    current_page_str = imglist[0][9:-1]
    current_page = string.atoi(current_page_str)#!!!!!
    return current_page

def total_page(html)
    reg = r'totalpage="[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    total_page_str = imglist[0][11:-1]
    total_page = string.atoi(total_page_str)
    return total_page
    
def get_page(url, curosr)
    html = urllib2.urlopen(url).read()
    html_utf8 = html.decode('gbk').encode('utf8')
    url_list = get_url(html_utf8)
    for url in url_list
        get_post(url, cursor)
    return
        if_end(html_utf8)
