#encoding=utf-8
import crawler
import time
import floor
import threading

class Post(object):
    def __init__(self, tid_list):
        self.lock = threading.Lock()
        self.tid_list = tid_list
        self.page = 1
        self.total_page = 1
        self.tid = 0
    def get(self):
        if self.tid == 0:
            self.lock.acquire()
            self.tid = self.tid_list.pop(0)
            self.lock.release()
        #self.tid = 3600061
        while self.page <= self.total_page:
            html = crawler.urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid='+str(self.tid)+'&page='+str(self.page))
            self.total_page = self.get_total_page(html)
            html = html[html.find('查看:'):]
            index = html.find('使用道具')
            while index != -1:
                floor.crawle(html[0:index], self.tid, self.lock)
                html = html[index+12:]
                index = html.find('使用道具')
            self.page += 1
        self.lock.acquire()
        crawler.post_finish()
        self.lock.release()
        self.page = 1
        self.total_page = 1
        self.tid = 0

    def crawle(self):
        time.sleep(60)
        while len(self.tid_list) != 0 or self.tid != 0:
            self.get()

    def get_total_page(self, html):
        html_tem = html
        index = html_tem.find('title="共')
        if index == -1:
            return 1
        else:
            html_tem = html_tem[index:]
            html_tem = html_tem[0:html_tem.find('页')]
            html_tem = html_tem[10:]
            total_page = int(html_tem)
        return total_page  
