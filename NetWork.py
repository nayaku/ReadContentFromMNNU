# -*- coding:utf-8 -*-

import urllib2
import Setting
import cookielib
import urllib


class NetWork:
    # 获取页面内容类
    opener = None

    # 初始化
    @staticmethod
    def set_up():
        cookie_jar = cookielib.LWPCookieJar()
        NetWork.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cookie_jar))  # urllib2.HTTPCookieProcessor(cookie_jar)
        urllib2.install_opener(NetWork.opener)  # 以后request的时候 会自动发送这个cookie

    # 连接到页面，并返回页面内容
    @staticmethod  # 静态方法
    def read_page(page_url, data = None):
        t_str = u"Read page: " + page_url
        print t_str

        # page_url.encode('utf-8')
        # page_url = urllib2.quote(page_url)
        # print page_url.__class__
        # print page_url
        # if data:
        #     data = urllib.urlencode(data)
        request = urllib2.Request(page_url)
        response = urllib2.urlopen(request, timeout = Setting.Time_Out)
        content = response.read().decode("utf-8", "ignore")

        # content = NetWork.opener.open(page_url, data).read().decode("utf-8", "ignore")

        # print content
        return content

    # post 并储存cookie
    @staticmethod
    def post(params, request_url):
        print u"post :" + request_url

        # 登入 获取cookie
        request = urllib2.Request(request_url)
        data = urllib.urlencode(params)
        response = NetWork.opener.open(request, data)
        content = response.read().decode('utf-8')
        # return cookie_jar
