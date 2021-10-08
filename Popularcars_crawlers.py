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
import csv
driver=webdriver.Chrome()
driver.get("https://www.dongchedi.com/auto/library/x-x-x-x-x-x-x-x-x-x-x")
#将滚动条移动到页面的底部
import time
driver.execute_script("window.scrollBy(0,3000)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,8000)")
time.sleep(1)

carinfo='data/carinfo.csv'
infols=[]
for i in range(1,101):
    car='//*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[{}]'.format(str(i))
    carid=driver.find_element_by_xpath(car+'/a').get_attribute('href')
    carid=carid.split('/')[-1]
    carname=driver.find_element_by_xpath(car+'/a/p[1]').text
    score=driver.find_element_by_xpath(car+'/a/div[2]/span[2]').text
    price=driver.find_element_by_xpath(car+'/a/p[2]').text
    infols.append([carid,carname,score,price])
with open(carinfo,mode='a',encoding='utf-8',newline='')as cf:
    writer=csv.writer(cf)
    writer.writerow(['carid','carname','score','price'])
    writer.writerows(infols)

# 全部汽车：//*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]
#//*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[2]
#carname //*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[1]/a/p[1]/text()
#score  //*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[1]/a/div[2]/span[2]
#href //*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[2]/a
#price //*[@id="__next"]/div[1]/div[2]/div/div/div/section/div[6]/ul/li[1]/a/p[2]






