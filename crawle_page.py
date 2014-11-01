#encoding=utf-8
import urllib
import urllib2
import re
import crawler
import crawle_post
import chardet

counter = 0

def get_url(html):
    reg = r'previewThread[\s\S]+?onclick'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for url in imglist:
        string = url
        string = string[string.find("viewthread"):]
        string = string[0:string.find('"')]
        string = 'http://bbs.hackbase.com/forum.php?mod='+string
        imglist[counter] = crawler.replace(string,'&amp;','&')
        counter += 1
    return imglist

def if_end(html):
    if current_page(html) == total_page(html):
        return 1
    else:
        return 0

def current_page(html):
    reg = r'curpage="[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(reg, html)
    current_page_str = imglist[0][9:-1]
    current_page = int(current_page_str)
    return current_page

def total_page(html):
    reg = r'totalpage="[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    total_page_str = imglist[0][11:-1]
    total_page = int(total_page_str)
    return total_page
    
def get_page(url):
    html = urllib2.urlopen(url).read()
    encode_dict = chardet.detect(html)
    if encode_dict['encoding'] == 'UFT-8' or encode_dict['encoding'] == 'utf-8':
        html = html
    else:
        html = html.decode('gbk','ignore').encode('utf8')

    url_list = get_url(html)
    tem_counter = 0
    for url in url_list:
        if tem_counter == crawle_post.counter:
            crawle_post.get_post(url)
            self.counter += 1
        tem_counter += 1
    self.counter = 0
    return if_end(html)
