#! /usr/python
#encoding=utf-8
import urllib
import urllib2
import re
import cookielib
import crawler

def get_loginhash(html):
    reg = r'loginhash[\s\S]+?"'
    imglist = crawler.regex(reg, html)
    loginhash = imglist[0][10:-1]
    return loginhash

def get_formhash(html):
    reg = r'formhash[\s\S]+?/'
    imglist = crawler.regex(reg, html)
    formhash = imglist[0][17:-3]
    return formhash

def get_seccode(html):
    reg = r'seccode[\s\S]+?"'
    imglist = crawler.regex(reg, html)
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
        print 'LOGIN FAIL'
        login()
    else:
        print 'LOGIN SUCCESS'

