import urllib
import urllib2
import re

html = urllib2.urlopen('LINKING').read()

html_utf8 = html.decode('gbk').encode('utf8')

reg = r'<div style="height:2px; overflow:hidden;">[\s\S]+?</div>'
imgre = re.compile(reg)
imglist = re.findall(reg, html_utf8)

