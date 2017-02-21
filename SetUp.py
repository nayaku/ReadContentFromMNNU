# -*- coding:utf-8 -*-

import Setting
import sys
import os

def run():
    print u"*******************************************************"
    print u"         Contest 提交代码批量获取工具。"
    print u"                                            版本：1.03"
    print u"                                           --- BY 雪靡"
    print u"*******************************************************"

    while Setting.User_Name == u'':
        print u"请输入用户名："
        Setting.User_Name = sys.stdin.readline().strip().decode('gbk')
    while Setting.Password == u'':
        print u"请输入密码："
        Setting.Password = sys.stdin.readline().strip().decode('gbk')

    print u"请输入要查询的contest正则表达式："
    print u'[默认="' + Setting.Contest_Title_Pattern2 + u'"]'
    text = sys.stdin.readline().strip().decode('gbk')
    if not text == u'':
        Setting.Contest_Title_Pattern2 = text

    print u"请输入要查询的contest的密码："
    print u'[默认="' + Setting.Contest_PassWord + u'"]'
    text = sys.stdin.readline().strip().decode('gbk')
    if not text == u'':
        Setting.Contest_PassWord = text

    print u"请输入文件存放的地址"
    print u'[默认="' + Setting.Path.decode('gbk') + u'"]'
    text = sys.stdin.readline().strip()
    if not text == u'':
        Setting.Path = text
        if not os.path.isdir(text):
            os.makedirs(text)

# run()
