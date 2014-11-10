#encoding=utf-8
import crawler
import pdb
import auth

def crawle(html, tid, lock):
    #pdb.set_trace()
    content = get_content(html)
    auth_id = get_id(html)
    date = get_date(html)
    if auth_id == -1:
        return
    try:
        auth_list = crawler.auth_set[auth_id]
    except:
        #pdb.set_trace()
        auth_list = []
        jdt_rp_my = auth.get_jdt_rp_my(auth_id)
        auth_list.append(get_name(html))
        auth_list.append(get_time(html))
        auth_list.append(get_value(html))
        auth_list.append(get_level(html))
        auth_list.append(jdt_rp_my[0])
        auth_list.append(jdt_rp_my[1])
        auth_list.append(jdt_rp_my[2])
        auth_list.append(get_post_num(html))
        auth_list.append(get_topic_num(html))
        try:
            crawler.auth_set[auth_id] = auth_list
        except:
            pass
    finally:
        cur_floor = get_floor(html)
        sql = ''
        try:
            if cur_floor == 1:
                title = get_title(html)
                view = get_view(html)
                reply = get_reply(html)
                #pdb.set_trace()
                sql = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('insert into main_post(post_id,post_title,post_view,post_reply,post_date,post_content,auth_id,auth_name,auth_join_date,auth_post_num,auth_topic_num,auth_time,auth_level,auth_values,auth_money,auth_reputation)values(',str(tid),',"',title,'","',view,'","',reply,'","',date,'","',content,'",',str(auth_id),',"',auth_list[0],'","',auth_list[4],'","',auth_list[7],'","',auth_list[8],'","',auth_list[1],'","',auth_list[3],'","',auth_list[2],'","',auth_list[6],'","',auth_list[5],'");')
            else:
                if cur_floor > 0:
                    sql = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('insert into post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_join_date,auth_post_num,auth_topic_num,auth_time,auth_level,auth_values,auth_money,auth_reputation)values(',str(tid),',',str(cur_floor),',"',date,'","',content,'",',str(auth_id),',"',auth_list[0],'","',auth_list[4],'","',auth_list[7],'","',auth_list[8],'","',auth_list[1],'","',auth_list[3],'","',auth_list[2],'","',auth_list[6],'","',auth_list[5],'");')
                else:
                    sql = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('insert into another_post_detail(post_id,post_floor,post_date,post_content,auth_id,auth_name,auth_join_date,auth_post_num,auth_topic_num,auth_time,auth_level,auth_values,auth_money,auth_reputation)values(',str(tid),',',str(crawler.floor),',"',date,'","',content,'",',str(auth_id),',"',auth_list[0],'","',auth_list[4],'","',auth_list[7],'","',auth_list[8],'","',auth_list[1],'","',auth_list[3],'","',auth_list[2],'","',auth_list[6],'","',auth_list[5],'");')
        except:
           print auth_list
        lock.acquire()
        crawler.insert(sql)
        crawler.floor_finish()
        lock.release()
#        print sql

def get_content(html):
    if html.find('<div class="locked">') != -1:
        return "内容自动屏蔽"
    else:
        html_tem = html
        index = html_tem.find('<div class="pcb">')
        html_tem = html_tem[index:]
        index=  html_tem.find('</table>')
        html_tem = html_tem[0:index]
        index = html_tem.find('</div>')
        if index != -1:
            html_tem = html_tem[index:]
        return content_cut(html_tem)

def content_cut(string):
    string = crawler.lable_cut(string)
    string = crawler.replace(string, '&nbsp;','')
    return string

def get_id(html):
    html_tem = html
    index = html_tem.find('authi"><')
    if index == -1:
        return -1
    else:
        html_tem = html_tem[index:]
        html_tem = html_tem[0 : html_tem.find('target')]
        html_tem = html_tem[html_tem.find('uid='):]
        return int(html_tem[4:-2])

def get_title(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('thread_subject'):]
    html_tem = html_tem[0:html_tem.find('</span>')]
    html_tem = html_tem[16:]
    return html_tem

def get_view(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('查看:'):]
    html_tem = html_tem[html_tem.find('&nbsp;')+6:]
    html_tem = html_tem[0:html_tem.find('&nbsp;')]
    return html_tem

def get_reply(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('回复:'):]
    html_tem = html_tem[html_tem.find('&nbsp;')+6:]
    html_tem = html_tem[0:html_tem.find('&nbsp;')]
    return html_tem

def get_name(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('xw1'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[html_tem.find('>')+1:]
    return html_tem

def get_value(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('积分</dt>'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[html_tem.find('xi2">')+5:]
    return html_tem

def get_date(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('发表于'):]
    html_tem = html_tem[0:html_tem.find('</em>')]
    html_tem = html_tem[10:]
    index = html_tem.find('title="')
    if index == -1:
        return html_tem
    else:
        html_tem = html_tem[index+7:]
        html_tem = html_tem[0:html_tem.find('"')]
        return html_tem

def get_time(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('color:#F00'):]
    html_tem = html_tem[0:html_tem.find('</dd>')]
    html_tem = html_tem[html_tem.find('>')+1:]
    return html_tem

def get_level(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('Rank:'):]
    html_tem = html_tem[0:html_tem.find('" />')]
    html_tem = html_tem[5:]
    try:
        return str(int(html_tem))
    except:
        print html_tem
        return str(1)

def get_topic_num(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('from=space'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[24:]
    return html_tem

def get_post_num(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('主题</th>'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[html_tem.find('xi2">')+5:]
    index = html_tem.find('title')
    if index == -1:
        return html_tem
    else:
        html_tem = html_tem[index+7:]
        html_tem = html_tem[0:html_tem.find('"')]
        return html_tem

def get_floor(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('帖子地址复制成功'):]
    html_tem = html_tem[0:html_tem.find('</em>')]
    html_tem = html_tem[48:]
    try:
        return int(html_tem)
    except:
        return -1
