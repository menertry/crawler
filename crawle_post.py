import urllib
import urllib2
import re
import get_auth

def get_auth_id(html)
    reg = r'avtm[\s\S]+?/'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    imglist.pop(-1)
    counter = 0
    for auth_id in imglist
        imglist[counter] = auth_id[81:-5]
        counter += 1
    return imglist

def get_auth_name(html)
    reg = r'"xw1[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for name in imglist
        imglist[counter] = name[name.find('>')+1:-4]
        counter += 1
    return imglist

def get_auth_time(html)
    reg = r'color:#F00[\s\S]+?</dd>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for time in imglist
        imglist[counter] = time[12:-5]
        counter += 1
    return imglist

def get_auth_value(html)
    reg = r'do=profile" target="_blank" class="xi2"[\s\S]+?</a>' 
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    value_list = []
    for value in imglist
        if counter%2  == 1:
            value_list.append(imglist[counter][40:-4])
        counter += 1
    return value_list

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

def get_post_topic(html)
    reg = r'from=space[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    post_num = topic_num =[]
    counter = 0
    for string in imglist
        if counter%2 == 0:
            post_num.append(imglist[counter][24:-4])
        else:
            topic_num.append(imglist[counter][24:-4])
        counter += 1
    return [post_num, topic_num]

def get_level(html)
    level = []
    string = html
    while string.find('Rank') != -1:
        index = string.find('Rank')
        string = string[index+6:]
        if index > 1000:
            level.append(string[0:string.find('"')])
    return level
    

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

def if_end(html)
    if current_page(html) != total_page(html)
        return 1
    else
        return 0

def current_page(html)
    reg = r'class="pg"[\s\S]+?</strong>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return string.atoi(imglist[0][19:-9])

def total_page(html)
    reg = r'title="共[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return string.atoi(imglist[0][11:-5])


def  get_post(url, cursor)
    html = urllib2.urlopen(url).read().decode('gbk').encode('utf8')

    post_id = get_post_id(html)
    post_title = get_title(html)
    content =get_content(html)
    vw_rp = get_view_reply(html)
    date = get_date(html)
    auth_id = get_auth_id(html)
    auth_name = get_auth_name(html)
    auth_time = get_auth_time(html)
    auth_value = get_auth_value(html)

    url_list = get_auth_url(html)

    auth_list = get_auth(url_list[0])
    sql = "".join("insert into main_post(post_id,post_title,post_view,post_reply,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values(",post_id,',"',post_title,'",',vw_rp[0],',',vw_rp[1],',"'date[0],'","',content[0],'",',auth_id[0],',"',auth_name[0],'","',auth_time[0],'","',auth_list[0],'",',auth_value[0],',',auth_list[1],',',auth_list[2],',',auth_level[0],',',post_num,',',topic_num,");")
    cursor.execute(sql)
    
    auth_list.pop(0)
    floor = 2
    for auth_url in url_list
        auth_list = get_auth(auth_url)
        sql = "".join("insert into post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values(",post_id,',',string.itoa(floor),',"'date[floor-1],'","',content[floor-1],'",',auth_id[floor-1],',"',auth_name[floor-1],'","',auth_list[0],'",',auth_value[floor-1],',',auth_list[1],',',auth_list[2],',',auth_level[floor-1],post,auth_list[8],auth_list[9]");"
        cursor.execute(sql)
        floor += 1
    return if_end(html_utf8)
