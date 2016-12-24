# -*- coding:utf-8 -*-

import sys

# 设置区域

# MNNU地址
MNNU_Url = u'http://acm.mnnu.edu.cn'
# 用户名
User_Name = u''
# 密码
Password = u''
# 超时时间
Time_Out = 60
# MNNU Contests页面
Contest_List_Url = MNNU_Url + u'/index.php/Contest/lists/s/all/p/'
# # 搜索页面前缀
# Search_Url_Prefix = MNNU_Url + u'/index.php/Contest/searchContest/title/'
# Search_Url_Suffix = u'/type/0/go/Search/'
# Contest_Title_Pattern = u'hwt2015级软件1班'
Contest_Title_Pattern2 = u'hwt2015级.*?软件1.*?作业'
# Contest密码
Contest_PassWord = u'mnnu'
# 当前路径
Path = sys.path[0]
