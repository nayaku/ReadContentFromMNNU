# -*- coding:utf-8 -*-
import sys

import Login
import ContestList
import NetWork
import SetUp

# 这里是主文件。用 python main.py 运行这个脚本
if __name__ == '__main__':
    SetUp.run()
    NetWork.NetWork.set_up()
    login = Login.Login()
    login.login()
    contest_list = ContestList.ContestList()
    contests = contest_list.get_contest_list2()
    for contest in contests:
        contest.post()
        contest.fetch_problem()
    print u'请输入任意按键结束程序。'
    sys.stdin.readline()
