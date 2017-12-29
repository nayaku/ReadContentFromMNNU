# -*- coding:utf-8 -*-

import requests


class NetWork:
    # 获取页面内容类
    # opener = None
    session = None
    headers = {
        'Host': 'acm.mnnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '14',
        'Origin': 'http://acm.mnnu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Test': 'testheadervalue',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://acm.mnnu.edu.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9' }

    # # 初始化
    @staticmethod
    def set_up():
        NetWork.session = requests.Session()
        #NetWork.session.headers.update(NetWork.headers)

    #     cookie_jar = cookielib.LWPCookieJar()
    #     NetWork.opener = urllib2.build_opener(
    #         urllib2.HTTPCookieProcessor(cookie_jar))  # urllib2.HTTPCookieProcessor(cookie_jar)
    #     urllib2.install_opener(NetWork.opener)  # 以后request的时候 会自动发送这个cookie

    # 连接到页面，并返回页面内容
    @staticmethod  # 静态方法
    def read_page(page_url):
        t_str = u"Read page: " + page_url
        print t_str

        # page_url.encode('utf-8')
        # page_url = urllib2.quote(page_url)
        # print page_url.__class__
        # print page_url
        # if data:
        #     data = urllib.urlencode(data)
        # request = urllib2.Request(page_url)
        # response = urllib2.urlopen(request, timeout = Setting.Time_Out)
        # content = response.read().decode("utf-8", "ignore")
        #
        # content = NetWork.opener.open(page_url, data).read().decode("utf-8", "ignore")

        # print content
        content = NetWork.session.get(page_url).text
        # print content
        return content

    # post 并储存cookie
    @staticmethod
    def post(params, request_url):
        print u"post :" + request_url

        # # 登入 获取cookie
        # request = urllib2.Request(request_url)
        # data = urllib.urlencode(params)
        # response = NetWork.opener.open(request, data)
        # print response
        # content = response.read().decode('utf-8')
        # print content
        # return cookie_jar
        content = NetWork.session.post(request_url, params,headers = NetWork.headers).text
# NetWork.set_up()
# print NetWork.post({'cpassword':'jkds'},'http://acm.mnnu.edu.cn/Contest/authprocess/cid/2755.htm')
# print "\n\n"
# print NetWork.read_page('http://acm.mnnu.edu.cn/Contest/plist/cid/2755.htm')