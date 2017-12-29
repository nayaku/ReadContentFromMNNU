# -*- coding:utf-8 -*-

import NetWork
import Setting
import re
import Contest


class ContestList:
    # contest list 类
    def __init__(self):
        self.contest_list = []  # contest 的列表

    # # 获取contest list
    # def get_contest_list(self):
    #     self.contest_list = [] # 清空列表
    #     title_pattern = Setting.Contest_Title_Pattern.encode('utf-8')
    #     title_pattern = urllib2.quote(title_pattern)
    #     search_url = Setting.Search_Url_Prefix.encode('utf-8') + title_pattern  + Setting.Search_Url_Suffix.encode('utf-8')
    #     page_num = self.get_page_num(search_url)
    #     for i in range(page_num):
    #         content = NetWork.NetWork.read_page(search_url + u'p/' + str(i).decode('utf-8'))
    #         #print content
    #         pattern = re.compile(u'''<td><a href="(.*?)">(.*?)</a></td>''',re.S)
    #         items = re.findall(pattern, content)
    #         for item in items:
    #             print item
    #             contest = Contest.Contest(item[1],item[0])
    #             self.contest_list.append(contest)
    #     return self.contest_list

    # 获取contest list OJ自带的搜索太差了，这里自己写搜索
    def get_contest_list2(self):
        self.contest_list = []  # 清空列表
        page_num = self.get_page_num(Setting.Contest_List_Url)
        for index in range(page_num):
            url = Setting.Contest_List_Url + str(index)
            content = NetWork.NetWork.read_page(url)
            pattern = re.compile(u'''<td><a href="(.*?)">(.*?)</a></td>''', re.S)
            items = re.findall(pattern, content)
            for item in items:
                if re.match(Setting.Contest_Title_Pattern2, item[1]):
                    print u"get contest name :" + item[1]
                    contest = Contest.Contest(item[1], item[0])
                    self.contest_list.append(contest)
        return self.contest_list

    # 获取页面数量
    def get_page_num(self, search_url):

        content = NetWork.NetWork.read_page(search_url)
        pattern = re.compile(u'''class='last' >... (.*?)</a>''', re.S)
        items = re.findall(pattern, content)
        if items:
            items = int(items[0])
            return items
        else:
            return 1
