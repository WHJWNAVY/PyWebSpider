import sys
import re
import time
import datetime
import os
import random
import requests
import csv
import lxml.html
from selenium import webdriver


class WebSpider(object):
    # user_agent列表，每次执行requests请求都随机使用该列表中
    WebUAList = [
        # Windows / Firefox 58
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0",
        # Linux / Firefox 58
        "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
        # Mac OS X / Safari 11.0.2
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_2) AppleWebKit/603.1.13 (KHTML, like Gecko) Version/11.0.2 Safari/603.1.13",
        # Windows / IE 11
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # Windows / Edge 16
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/16.16299.15.0",
        # Windows / Chrome 63
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        # Android Phone / Chrome 63
        "Mozilla/5.0 (Linux; Android 7.0; SM-G935P Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
        # Android Tablet / Chrome 63
        "Mozilla/5.0 (Linux; Android 4.4.4; Lenovo TAB 2 A10-70L Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36",
        # iPhone / Safari 11.1.1
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/11.1.1 Mobile/14E304 Safari/602.1",
        # iPad / Safari 11.1.1
        "Mozilla/5.0 (iPad; CPU OS 11_1_1 like Mac OS X) AppleWebKit/603.3.3 (KHTML, like Gecko) Version/11.1.1 Mobile/14G5037b Safari/602.1"]

    def __init__(self, use_browser=False, browser="Chrome", timeout=20, debug=True):
        self.__WebDriver = None
        self.__WebBrowser = browser
        self.__TimeOut = timeout
        self.__DebugOn = debug
        self.__UseBrowser = use_browser

        # web请求头
        self.WebHeader = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }

        if self.__UseBrowser == True:
            # self.__WebDriver = self.__WebDriverInit(self.__TimeOut)
            self.__WebDriverInit(self.__TimeOut)

    def __del__(self):
        if self.__UseBrowser == True:
            self.__WebDriverExit()
        self.__Debug("Exit...")

    def __Debug(self, outs):
        if self.__DebugOn == True:
            print(outs)

    # 字符串转码编译
    def __Decode(self, s):
        return s.encode('gbk', 'ignore').decode('gbk', 'ignore')

    # #去掉非法字符
    def __NameFilter(self, s):
        return re.sub('[ \\/:*?"<>|\r\n]', '-', s) # 去掉非法字符

    def __AutoPath(self, path_name=None):
        filepath = os.path.join(os.path.expanduser("~"), 'Desktop')
        if path_name == None:
            datestr = datetime.datetime.now().strftime("%Y-%m-%d")
            filepath = os.path.join(filepath, datestr)
        else:
            path_name = self.__NameFilter(path_name)
            filepath = os.path.join(filepath, path_name)
        if os.path.exists(filepath) != True:
            os.makedirs(filepath)  # 如果指定的文件夹不存在就递归创建
        return filepath

    def __AutoName(self, file_name=None, ext='txt'):
        if file_name == None:
            timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = "{0}.{1}".format(timestr, ext)
        else:
            file_name = self.__NameFilter(file_name)
            filename = "{0}.{1}".format(file_name, ext)
        return filename

    def __FilePath(self, path_name=None, file_name=None, ext='txt'):
        fpath = self.__AutoPath(path_name)
        fname = self.__AutoName(file_name, ext)
        fullpath = os.path.join(fpath, fname)
        return fullpath

    def __WebDriverInit(self, timeout=20):
        if self.__WebDriver == None:
            if self.__WebBrowser == "Chrome":
                coptions = webdriver.ChromeOptions()
                coptions.headless = True
                # coptions.add_argument('--headless')  # 无头参数
                # coptions.add_argument('--disable-gpu')
                # 配了环境变量第一个参数就可以省了，不然传绝对路径
                self.__WebDriver = webdriver.Chrome(options=coptions)
                self.__WebDriver.implicitly_wait(timeout)
            elif self.__WebBrowser == "Firefox":
                foptions = webdriver.FirefoxOptions()
                foptions.headless = True
                # foptions.add_argument('-headless')  # 无头参数
                # 配了环境变量第一个参数就可以省了，不然传绝对路径
                self.__WebDriver = webdriver.Firefox(options=foptions)
                self.__WebDriver.implicitly_wait(timeout)
            elif self.__WebBrowser == "Edge":
                self.__WebDriver = webdriver.Edge()
                self.__WebDriver.implicitly_wait(timeout)
            else:
                self.__Debug(
                    "Invalid Browser Type [{0}]".format(self.__WebBrowser))

    def __WebDriverExit(self):
        if self.__WebDriver != None:
            self.__WebDriver.close()

    # 使用selenium下载页面
    def __WebDriverGet(self, url):
        htmlpage = None
        if url == None or len(url) == 0:
            self.__Debug('Please use a valid url!')
            return None
        try:
            self.__WebDriver.get(url)
            htmlpage = self.__WebDriver.page_source
        except:
            self.__Debug("get webpage {0} error".format(url))
        finally:
            return htmlpage

    # 使用requests下载页面
    def __RequestsGet(self, url):
        phtml = None
        page = None
        if url == None or len(url) == 0:
            self.__Debug('Please use a valid url!')
            return None
        try:
            # 选择一个随机的User-Agent
            self.WebHeader["User-Agent"] = random.choice(
                WebSpider.WebUAList)
            # requests请求得到页面
            page = requests.get(url=url, headers=self.WebHeader,
                                timeout=self.__TimeOut)  # 请求指定的页面
            # 打印页面的编码方式
            self.__Debug("page.encoding = [{0}]".format(page.encoding))
            if page.encoding == "ISO-8859-1":
                page.encoding = "utf-8"  # "gb2312"  # 转换页面的编码为gb2312(避免中文乱码)
            phtml = page.text  # 提取请求结果中包含的html文本
            self.__Debug("requests success")
            # page.close()  # 关闭requests请求
        # 抛出异常
        except requests.exceptions.RequestException as e:
            self.__Debug("requests error:[{0}]".format(e))
            phtml = None
            # if page != None:
            #     page.close()
        finally:
            if page != None:
                page.close()
            return phtml

    # 使用requests下载文件
    def GetFile(self, furl, fpath='auto', fname='auto'):
        """
        Download files using requests.

        :Args:
         - furl: file url
         - fpath: file save path. If it is <auto>, we will automatically selected a 
            path(usually the folder named on the desktop with the current date).
         - fname: file save name. if it's <auto>, we will automatically selected a 
            path from url.

        :Usage:
            You need to set <ws.WebHeader> first to download file!
            ws.GetFile('https://www.xxx.com/aaa.jpg', 'D:/Jpgs')
        """
        if furl == None or len(furl) == 0:
            self.__Debug('Please use a valid file url!')
            return
        if fpath == 'auto':
            fpath = self.__AutoPath()
        else:
            fpath = self.__AutoPath(fpath)
        if fname == 'auto':
            fname = os.path.basename(furl)  # 从url中提取文件名
        fresp = None
        try:
            if os.path.exists(fpath) != True:
                os.makedirs(fpath)  # 如果指定的文件夹不存在就递归创建

            ffull_path = os.path.join(fpath, fname)

            if os.path.isfile(ffull_path) == True:  # 判断文件是否存在
                self.__Debug('file <{0}> is exists'.format(ffull_path))
                return

            # 选择一个随机的User-Agent
            self.WebHeader["User-Agent"] = random.choice(WebSpider.WebUAList)

            fresp = requests.get(
                furl, headers=self.WebHeader, timeout=self.__TimeOut)  # 获取的文本实际上是图片的二进制文本
            fdata = fresp.content  # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本

            with open(ffull_path, 'wb') as ff:
                ff.write(fdata)  # 把图片数据写入文件。with语句会自动关闭f
            self.__Debug("save file to :{0}".format(ffull_path))
        except requests.exceptions.RequestException as e:
            self.__Debug(
                "download file {0} error, exceptions[{1}]".format(fname, e))
        finally:
            if fresp != None:
                fresp.close()

    def Gethtml(self, url):
        """
        Download html page using requests or selenium.

        :Args:
         - url: html page url

        :Usage:
            html = ws.Gethtml("https://www.ithome.com/")
        """
        if self.__UseBrowser == True:
            return self.__WebDriverGet(url)
        else:
            return self.__RequestsGet(url)

    def FilterHtml(self, p_html, x_path, decode=False):
        """
        Filter the data we want from the html page.

        :Args:
         - p_html: html page souce.
         - x_path: lxml XPATH.
         - decode: Whether to decode GBS to prevent garbled code.

        :Usage:
            html = ws.Gethtml("https://www.ithome.com/", False)
            ws.FilterHtml(html, '//div[@class="refreshnewslist"]/div/ul/li/span/a/@href')
        """
        p_type = type(p_html)
        if p_type == str:
            e_tree = lxml.html.fromstring(p_html)
        elif p_type == lxml.html.HtmlElement:
            e_tree = p_html
            self.__Debug("type(p_html) = {0}".format(e_tree))
        else:
            self.__Debug('Invalid type of <p_html>')
            return None
        clist = e_tree.xpath(x_path)
        if decode == True:
            for i in range(len(clist)):
                clist[i] = self.__Decode(clist[i])
        self.__Debug('html content list len[{0}]'.format(len(clist)))
        return clist

    def FilterAll(self, p_html, x_path, decode=False):
        content = ""
        flist = self.FilterHtml(p_html, x_path, decode)
        for fl in flist:
            content += fl
        return content

    # 将字典写入csv文件

    def Save(self, row, fname="auto"):
        """
        Save a list to csv file.

        :Args:
         - row: list to save.
         - fname: the file csv name to save.
        :Return:
            fname: the file csv name to save.
        :Usage:
            fname = ws.Save(dheader)
            ws.Save(dlist, fname=fname)
        """
        if fname == "auto":
            fname = self.__FilePath(ext='csv')
        else:
            fname = self.__FilePath(file_name=fname, ext='csv')
        with open(fname, 'a', newline='') as csvf:
            f_csv = csv.writer(csvf)
            f_csv.writerow(row)
        return fname

    def Wait(self):
        web_sleep = random.randint(1, 5)  # 延时一个随机值，避免被服务器反爬
        self.__Debug("waiting {0} seconds".format(web_sleep))
        time.sleep(web_sleep)


if __name__ == "__main__":
    ws = WebSpider()
    # print(ws.WebHeader["Accept"])
    # print(ws.WebHeader["User-Agent"])

    html = ws.Gethtml("https://www.ithome.com/")
    # print(html)

    herf = ws.FilterHtml(
        html, '//div[@class="refreshnewslist"]/div/ul/li/span/a/@href')
    text = ws.FilterHtml(
        html, '//div[@class="refreshnewslist"]/div/ul/li/span/a/text()', decode=True)
    dlen = len(herf)
    for i in range(dlen):
        print(i, text[i], herf[i])

    # print(ws.FilterAll(
    #     html, '//div[@class="refreshnewslist"]/div/ul/li/span/a/@herf'))
    # print(ws.FilterAll(
    #     html, '//div[@class="refreshnewslist"]/div/ul/li/span/a/text()', decode=True))
