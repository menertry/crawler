import urllib
import urllib2
import re
import MySQLdb

#html = urllib2.urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid=3598460&extra=page%3D1').read();
#get html page

#reg = r'<table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_.+?</table>'


db = MySQLdb.connect("localhost","root","","mysql")
cursor = db.cursor()

url = ""
page_url = url
html = urllib2.urlopen(page_url)
page = 1

while get_page(page_url) != 1
    page += 1
    page_url = url + "&page=" + string.itoa(page)

db.commit()
db.close()
