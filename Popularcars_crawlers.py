# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 11:13
# @Author  : yumh
# @Site    : Shenyang
# @File    : Popularcars_crawlers.py
# @Software: PyCharm
#热门车型爬虫
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.dongchedi.com/auto/library/x-x-x-x-x-x-x-x-x-x-x")
#将滚动条移动到页面的底部
import time
driver.execute_script("window.scrollBy(0,3000)")
time.sleep(1)



