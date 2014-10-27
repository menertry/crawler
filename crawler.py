import urllib
import urllib2
import re
import time

#html = urllib2.urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid=3598460&extra=page%3D1').read();
#get html page

#reg = r'<table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_.+?</table>'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
    def handle_comment(self, data):
        print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data

parser = MyHTMLParser()

