# -*- coding:utf-8 -*-

import Setting
import NetWork


class Login:
    # 登入类

    def login(self):
        # 登入 获取cookie
        loginparams = {"username": Setting.User_Name, "password": Setting.Password}
        request_url = 'http://acm.mnnu.edu.cn/User/chklogin.htm'
        NetWork.NetWork.post(loginparams, request_url)
