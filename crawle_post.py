#encoding=utf-8
import urllib
import urllib2
import re
import crawle_auth
import crawler
import chardet

counter = 0

def get_auth_id(html):
    reg = r'authi"><[\s\S]+?target'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for auth_id in imglist:
        imglist[counter] = auth_id[43:-8]
        counter += 1
    return imglist

def get_auth_name(html):
    reg = r'"xw1[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for name in imglist:
        imglist[counter] = name[name.find('>')+1:-4]
        counter += 1
    return imglist

def get_auth_time(html):
    reg = r'color:#F00[\s\S]+?</dd>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for time in imglist:
        imglist[counter] = time[12:-5]
        counter += 1
    return imglist

def get_auth_value(html):
    reg = r'do=profile" target="_blank" class="xi2"[\s\S]+?</a>' 
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    value_list = []
    for value in imglist:
        if counter%2  == 1:
            value_list.append(imglist[counter][40:-4])
        counter += 1
    return value_list

def get_title(html):
    reg = r'<span id="thread_subject">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_title = imglist[0][26:-7]
    return str_title

def get_content(html):
    reg = r'<div class="pcb">[\s\S]+?</table>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for str_content in imglist:
        imglist[counter] = content_cut(str_content[:-5])
        counter += 1
    return imglist

def content_cut(string):
    index = string.find('</div>')
    if index != -1:
        string = string[index+6:]
    string = lable_cut(string)
    string = crawler.replace(string, '&nbsp;','')
    return string

def lable_cut(string):#BUG!!!!!
    reg = r'<[\s\S]+?>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, string)
    for cut in imglist:
        index = string.find(cut)
        string = string[0:index]+string[index+len(cut):]
    return string

def get_post_id(html):
    reg = r'tid=[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_id = imglist[0][4:-1]
    return str_id

def get_date(html):
    reg = r'<em id="authorposton[\s\S]+?</em>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    #str_id = imglist[0][20:-35]
    counter = 0
    for str_date in imglist:
        imglist[counter] = str_date[-24:-5]
        counter += 1
    return imglist

def get_post_topic(html):
    reg = r'from=space[\s\S]+?</a>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    post_num = []
    topic_num = []
    counter = 0
    for string in imglist:
        if counter%2 == 0:
            topic_num.append(lable_cut(imglist[counter][24:-4]))
        elif counter%2 == 1:
            post_num.append(lable_cut(imglist[counter][24:-4]))
        counter += 1
    return [post_num, topic_num]

def get_level(html):
    reg = r'gid=[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    imglist.pop(0)
    counter = 0
    for level in imglist:
        imglist[counter] = str(15-int(level[4:-1]))
        counter += 1
    return imglist
    
def get_floor(html):
    reg = r'帖子地址复制成功[\s\S]+?</'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    counter = 0
    for floor in imglist:
        imglist[counter] = floor[48:-2]
        if floor[48:-2][-1] == '\n':
            imglist[counter] = '@'
        counter += 1
    return imglist

def get_view_reply(html):
    reg = r'<span class="xi1">[\s\S]+?</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    str_view = imglist[0][24:-13]
    str_reply = imglist[1][24:-13]
    return [str_view, str_reply]

def get_auth_url(html, auth_id):
    uid = auth_id
    counter = 0
    url_list = []
    for url in uid:
        url_list.append( "http://bbs.hackbase.com/home.php?mod=space&uid="+uid[counter]+"&do=profile")
        counter += 1
    return url_list

def if_end(html):
    if current_page(html) == total_page(html):
        return 1
    else:
        return 0

def current_page(html):
    reg = r'class="pg"[\s\S]+?</strong>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    if len(imglist) == 0:
        return 1
    else:
        return int(imglist[0][19:-9])

def total_page(html):
    reg = r'title="共[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    if len(imglist) == 0:
        return 1
    else:
        return int(imglist[0][11:-5])


def  get_post(url):
    html = urllib2.urlopen(url).read()
    encode_dict = chardet.detect(html)
    if encode_dict['encoding'] == 'UFT-8' or encode_dict['encoding'] == 'utf-8':
        html = html
    else:
        html = html.decode('gbk','ignore').encode('utf8')
        

    post_id = get_post_id(html)
    post_title = get_title(html)
    content = get_content(html)
    vw_rp = get_view_reply(html)
    date = get_date(html)
    floor = get_floor(html)
    auth_level = get_level(html)
    auth_id = get_auth_id(html)
    auth_name = get_auth_name(html)
    auth_time = get_auth_time(html)
    auth_value = get_auth_value(html)
    post_topic = get_post_topic(html)

    url_list = get_auth_url(html, auth_id)

    tem_counter = 0
    if self.counter == tem_counter:
        auth_list = crawle_auth.get_auth(url_list[0])
        sql = 'insert into main_post(post_id,post_title,post_view,post_reply,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values('+post_id+',"'+post_title+'","'+vw_rp[0]+'","'+vw_rp[1]+'","'+date[0]+'","'+content[0]+'",'+auth_id[0]+',"'+auth_name[0]+'","'+auth_time[0]+'","'+auth_list[0]+'","'+auth_value[0]+'","'+auth_list[1]+'","'+auth_list[2]+'","'+auth_level[0]+'","'+post_topic[0][0]+'","'+post_topic[1][0]+'");'
        print sql
        crawler.insert(sql)
    
        self.post_counter += 1
        print crawler.post_counter
 
    url_list.pop(0)
    tem_counter += 1
    for auth_url in url_list:
        if tem_counter == crawle_post.counter:
            auth_list = crawle_auth.get_auth(auth_url)
            if floor[counter][-1] == '@':
                sql = 'insert into another_post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values('+post_id+',"'+str(counter)+'","'+date[counter]+'","'+content[counter]+'",'+auth_id[counter]+',"'+auth_name[counter]+'","'+auth_time[counter]+'","'+auth_list[0]+'","'+auth_value[counter]+'","'+auth_list[1]+'","'+auth_list[2]+'","'+auth_level[counter]+'","'+post_topic[0][counter]+'","'+post_topic[1][counter]+'");'
            else:
                sql = 'insert into post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_time,auth_join_date,auth_value,auth_reputation,auth_money,auth_level,auth_post_num,auth_topic_num)values('+post_id+',"'+floor[counter]+'","'+date[counter]+'","'+content[counter]+'",'+auth_id[counter]+',"'+auth_name[counter]+'","'+auth_time[counter]+'","'+auth_list[0]+'","'+auth_value[counter]+'","'+auth_list[1]+'","'+auth_list[2]+'","'+auth_level[counter]+'","'+post_topic[0][counter]+'","'+post_topic[1][counter]+'");'
            print sql
            crawler.insert(sql)
            crawle_post.counter += 1

        tem_counter += 1
        self.post_counter += 1
        print crawler.post_counter
    self.post_counter = 0
    return if_end(html)
