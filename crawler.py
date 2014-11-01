import urllib
import urllib2
import re
import chardet

post = 0
floor = 0

def get_a_post():
    return urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid=2831312&extra=page%3D2')

def regex(reg, html):
    imgre = re.compile(reg)
    return re.findall(imgre, html)

def lable_cut(string):
    reg = r'<[\s\S]+?>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, string)
    for cut in imglist:
        index = string.find(cut)
        string = string[0:index]+string[index+len(cut):]
    return string

def urlopen(url):
        html = urllib2.urlopen(url).read()
        encode_dict = chardet.detect(html)
        if encode_dict['encoding'] == 'UFT-8' or encode_dict['encoding'] == 'utf-8':
            html = html
        else:
            html = html.decode('gbk','ignore').encode('utf8')
        return html
    except:
        return urlopen(url)

def get_loginhash(html):
    reg = r'loginhash[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    loginhash = imglist[0][10:-1]
    return loginhash

def get_formhash(html):
    reg = r'formhash[\s\S]+?/'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    formhash = imglist[0][17:-3]
    return formhash

def get_seccode(html):
    reg = r'seccode[\s\S]+?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    seccode = imglist[8:-1]
    return seccode

def login():
    try:
        loginurl = 'http://bbs.hackbase.com/member.php?mod=logging&action=login'
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        html = urllib2.urlopen(loginurl).read()
        posturl = 'http://bbs.hackbase.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash='+get_loginhash(html)+'&inajax=1'
        data ={'formhash':get_formhash(html),'referer':'http://bbs.hackbase.com/forum.php','username':'menertry','password':'8e4ca7af923595919610e17f0dde5140','questionid':'0','answer':'','seccodehash':get_seccode(html),'seccodemodid':'member::logging','seccodeverify':''}
        post_data = urllib.urlencode(data)
        req = urllib2.Request(posturl,post_data)
        urllib2.urlopen(req)
    except:
        login()
    else:
        print LOGIN SUCESS!
