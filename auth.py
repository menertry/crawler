#encoding=utf-8
import crawler

def get_jdt_rp_my(auth_id):
    url = 'http://bbs.hackbase.com/home.php?mod=space&uid='+str(auth_id)+'&do=profile'
    html = crawler.urlopen(url)
    join_date = get_join_date(html)
    reputation = get_reputation(html)
    money = get_money(html)
    return [join_date, reputation, money]

def get_join_date(html):
    html_tem = html
    try:
        html_tem = html_tem[html_tem.find('注册时间'):]
        html_tem = html_tem[0:html_tem.find('</li>')]
        html_tem = html_tem[17:]
        return html_tem
    except:
        return '无'

def get_reputation(html):
    html_tem = html
    try:
        html_tem = html_tem[html_tem.find('威望</em>'):]
        html_tem = html_tem[0:html_tem.find('</li>')]
        html_tem = html_tem[11:]
        return html_tem
    except:
        return '无'
    
def get_money(html):
    html_tem = html
    try:
        html_tem = html_tem[html_tem.find('黑币</em>'):]
        html_tem = html_tem[0:html_tem.find('</li>')]
        html_tem = html_tem[11:]
        return html_tem
    except:
        return '无'
