#encoding=utf-8
import cwl_lib

class post(object):
    def __init__(self, tid_list):
        self.tid_list = tid_list
        self.page = 1
        self.total_page = 1
        self.tid = 0
    def get(self):
        try:
            if self.tid == 0:
                tid = self.tid_list.pop(0)
            while self.page <= self.total_page:
                html = cwl_lib.urlopen('http://bbs.hackbase.com/forum.php?mod=viewthread&tid='+str(tid)+'&extra=page='+str(self.page))
                self.total_page = self.total_page(html)
                html = html[index : html.find('查看:')]
                index = html.find('使用道具')
                while index != -1:
                    floor.get(html[0:index], self.tid)
                    html = html[index+12:]
                    index = html.find('使用道具')
                self.page += 1
            cwl_lib.post_finish()
            self.page = 1
            self.total_page = 1
            self.tid = 0
        except:
            pass

    def crawle(self):
        while 1:
            self.get()



def get_content(html):
    reg = r'<div class="pcb">[\s\S]+?</table>'
    content = cwl_lib.regex(reg, html)
    counter = 0
    for str_content in content:
        content[counter] = content_cut(str_content[:-8])
        counter += 1
    return imglist

def content_cut(string):
    index = string.find('</div>')
    if index != -1:
        string = string[index+6:]
    string = cwl_lib.lable_cut(string)
    string = cwl_lib.replace(string, '&nbsp;','')
    return string

