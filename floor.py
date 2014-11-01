#encoding=utf-8
import crawler

def get(html):
    content = get_content(html)
    auth_id = get_id(html)
    if auth_id == -1:
        return
    try:
        auth = crawler.auth_list[auth_id]
    except:
        auth = []
        jdt_rp_my = get_jdt_rp_my(auth_id)
        auth.append('name': get_name(html))
        auth.append('time': get_time(html))
        auth.append('value': get_value(html))
        auth.append('level': get_level(html))
        auth.append('join_date': jdt_rp_my[0])
        auth.append('reputation': jdt_rp_my[1])
        auth.append('money': jdt_rp_my[2])
        auth.append('post_num': get_post_num(html))
        auth.append('topic_num': get_topic_num(html))
        if post_topic[0]+post_topic[1] >= 10:
            crawler.auth_list.append(auth_id : auth)
    finally:
        floor = get_floor(html)
        if floor == 1:
            view = get_view(html)
            reply = get_reply(html)
            sql = """ """
        else:
            if floor > 0:
                sql = """ """
            else:
                sql = """ """
        crawler.insert(sql)


def get_content(html):
    if html.find('<div class="locked">'):
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
    string = cwl_lib.lable_cut(string)
    string = cwl_lib.replace(string, '&nbsp;','')
    return string

def get_auth_id(html):
    html_tem = html
    index = html_tem.find('authi"><')
    if html == -1:
        return -1
    else:
        html_tem = html_tem[index:]
        html_tem = html_tem[0 : html_tem.find('target')]
        html_tem = html_tem[html_tem.find('uid=')]
        return int(html_tem[4:-2])

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
    return html_tem

def get_topic_num(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('from=space'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[24:]
    return html_tem

def get_post_num(html):
    html_tem = html
    html_tem = html_tem[html_tem.find('主题'):]
    html_tem = html_tem[0:html_tem.find('</a>')]
    html_tem = html_tem[html_tem.find('xi2">')+5:]
    return html_tem
