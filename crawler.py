import urllib
import urllib2
import re
import MySQLdb
import login
import crawle_page

db = MySQLdb.connect("localhost","root","","mysql")
cursor = db.cursor()

login.login()

url = ""
page_url = url
html = urllib2.urlopen(page_url)
page = 1

while crawle_page.get_page(page_url, cursor) != 1
    page += 1
    page_url = url + "&page=" + string.itoa(page)

db.commit()
db.close()
