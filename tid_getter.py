#encoding=utf-8
import crawler

class Tid_getter(object):
    def __init__(self, url):
        self.total_page = 1 
        self.page = 1
        self.tid_list = []
        self.url = url
    
    def crawle(self):
        while self.page <= self.total_page:
            page_url = self.url + '&page=' + str(self.page)
            html = crawler.urlopen(page_url)
            self.total_page = self.get_total_page(html)
            reg = r'previewThread[\s\S]+?,'
            pre_tid = crawler.regex(reg, html)

            for tid in pre_tid:
                self.tid_list.append(tid[15:-2])
            self.page += 1

    def get_total_page(self, html):
        html_tem = html
        index = html_tem.find('title="共')
        if index == -1:
            return 1
        else:
            html_tem = html_tem[index:]
            html_tem = html_tem[0:html_tem.find('页')]
            html_tem = html_tem[10:]
        return int(html_tem)   
