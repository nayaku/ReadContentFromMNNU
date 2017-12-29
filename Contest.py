# -*- coding:utf-8 -*-


import re
import NetWork
import Setting
import Problem
import os



class Contest:
    # Contest类
    def __init__(self, title=u'', url=u''):
        self.title = title
        # self.title = title.decode('utf-8')  # 标题
        self.url = Setting.MNNU_Url + url  # url链接
        self.problem_list = []  # 问题列表

    def post(self):
        # post 登入
        params = {"cpassword": Setting.Contest_PassWord}
        request_url = self.url.replace("explain", "authprocess")
        NetWork.NetWork.post(params, request_url)

    def get_status(self):
        print "self.url " + self.url
        status_url = self.url.replace("explain", "status")
        print status_url
        content = NetWork.NetWork.read_page(status_url)

    # 获取问题
    def fetch_problem(self):
        print self.title
        title = self.title.replace(u'—', u'')
        print title
        title = title.replace(u'\\', u'、').replace(u'/', u'、').replace(u':', u'：').replace(u'*', u' ').replace(u'"', u'\'') \
            .replace(u'?', u'？').replace(u'<', u'《').replace(u'>', u'》').replace(u'|', u'、')
        title = title.encode("gb2312")

        path = Setting.Path + "\\" + title
        print path
        if not os.path.exists(path):
            os.mkdir(path)

        url = self.url.replace('explain', 'plist')
        content = NetWork.NetWork.read_page(url)
        pattern = re.compile(u'''<td><a href="(.*?)">(.*?)</a></td>''', re.S)
        items = re.findall(pattern, content)
        idx = 1001
        for item in items:
            print u'item:' + str(idx).decode('utf-8'), item[1], item[0]
            problem = Problem.Problem(str(idx).decode('utf-8'), item[1], item[0])
            problem.fetch_status(self.url, path)  # 开始写入问题
            self.problem_list.append(problem)
            idx += 1
