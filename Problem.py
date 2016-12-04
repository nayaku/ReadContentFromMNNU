# -*- coding:utf-8 -*-

import HTMLParser
import codecs
import re
import Setting
import NetWork


class Problem:
    # 处理每个问题
    def __init__(self, id = u'', name = u'', url = u''):
        self.id = id  # 题目的id号
        self.name = name  # 题目名字
        self.url = url  # 题目url
        self.code = u''  # 设置提交的代码

    # 获取题目状态，传入一个网页url和目录路径
    def fetch_status(self, prefix_url, contest):
        url = prefix_url.replace('explain', 'status')
        url = url.replace('.htm', '/proid/' + self.id + '/username/' + Setting.User_Name + '/result/1/language/0/')
        content = NetWork.NetWork.read_page(url)
        # print content
        pattern = re.compile(u'''style="color:red;">.*?<a href='(.*?)'>.*?B</a>''', re.S)
        items = re.findall(pattern, content)
        if items:
            if not isinstance(items, (str, unicode)):
                items = items[0]

            items = Setting.MNNU_Url + items
            codes = self.read_code(items)
            codes = self.format_codes(codes)
            self.write_code(contest, codes)

    # 读取代码
    def read_code(self, url):
        content = NetWork.NetWork.read_page(url)
        pattern = re.compile('color:#EEEEEE;">(.*?)</pre>', re.S)
        item = re.findall(pattern, content)
        item = item[0]
        return item

    # 格式化获取的代码
    def format_codes(self, codes):

        html_parser = HTMLParser.HTMLParser()
        codes = html_parser.unescape(codes)  # 处理HTML转义字符
        return codes

    # 写入代码到文件
    def write_code(self, path, codes):
        path = path + "\\" + self.id.encode('gb2312') + '.cpp'
        file = codecs.open(path, 'w', 'utf-8')
        file.write(codes)
        file.close()
