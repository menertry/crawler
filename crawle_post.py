import urllib
import urllib2
import re

def get_title(html)
    reg = r'<span id="thread_subject">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_title = imglist[0][26:-7]
    return str_title

def get_content(html)
    reg = r'<div style="height:2px; overflow:hidden;">[\s\S]+?</div>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for str_content in imglist
        imglist[counter] = content_cut(str_content)
        counter += 1
    return imglist

def content_cut(string)
    content = string[42:-14]
    cut = "<br />"
    index = content.find(cut)
    while index != -1
        string = string[0:index]+string[index+len(cut):]
    return content

def get_post_id(html)
    reg = r'tid=[\s\S]+?"'#not test!!!
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][4:-1]
    return str_id

def get_date(html)
    reg = r'<em id="authorposton[\s\S]+?</em>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    #str_id = imglist[0][20:-35]
    counter = 0
    for str_date in imglist
        imglist[counter] = str_date[-23:-5]
        counter += 1
    return imglist

def get_view_reply(html)
    reg = r'<span class="xi1">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_view = imglist[0][24:-13]
    str_reply = imglist[1][24:-13]
    return [str_view, str_reply]

def get_auth_url
    reg = r'src="http[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    imglist.pop(0)
    imglist.pop()
    counter = 0
    for url in imglist
        uid = url[54:-13]
        imglist[counter] = "http://bbs.hackbase.com/home.php?mod=space&uid="+uid+"&do=profile"
        counter += 1
    return imglist

def get_post(url, cursor)
    html = urllib2.urlopen(url).read()
    html_utf8 = html.decode('gbk').encode('utf8')

    title = get_title(html_utf8)
    content =get_content(html_utf8)
    post_id = get_post_id(html_utf8)
    vw_rp = get_view_reply(html_utf8)
    date = get_date(html_utf8)

    url_list = get_auth_url(html_utf8)

    auth_list = get_auth(url_list[0])
    sql = "".join("insert into main_post(post_id,post_title,post_view,post_reply,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values(",post_id,title,vw_rp[0],vw_rp[1],date[0],content[0],auth_list[0],auth_list[1],auth_list[2],auth_list[3],auth_list[4],auth_list[5],auth_list[6],auth_list[7],auth_list[8],auth_list[9]");")
    cursor.execute(sql)
    
    auth_list.pop(0)
    floor = 2
    for auth_url in url_list
        auth_list = get_auth(auth_url)
        sql = "".join("insert into post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values(",post_id,string.itoa(floor),date[floor-1],content[floor-1],auth_list[0],auth_list[1],auth_list[2],auth_list[3],auth_list[4],auth_list[5],auth_list[6],auth_list[7],auth_list[8],auth_list[9]");"
        cursor.execute(sql)
        floor += 1
    return if_end(html_utf8)
