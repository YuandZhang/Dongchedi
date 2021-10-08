# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 13:15
# @Author  : yumh
# @Site    : 
# @File    : prepare_data.py.py
# @Software: PyCharm

from lxml import etree
import unicodedata
import html
import re
import jieba
from utlis.Configuration import Config
import base64
def remove_html(content,isdecode=None):#isdecode 判断是否先需要解码,需要解码为1
    """移除html标签"""
    # &#x等编码问题
    if isdecode==1:
        content=base64.b64decode(content).decode(encoding='utf-8')#内容解码
    content = html.unescape(content)
    content = unicodedata.normalize('NFKD', content)
    # 将html的换行替换成字符换行
    selector = etree.HTML(content)
    str_list = selector.xpath('//text()')
    text = ''.join(str_list)
    # text = clean(text)#数据清理
    text = clean(text)  # 去除英文和标点
    text=remove_stopwords(text)

    return text

def clean(text):
    text = re.sub('[^\u4e00-\u9fa5]+', '', text)
    return text

def remove_stopwords(text):
    stopwords = [i.strip() for i in open(Config.stopwords_file,encoding='utf-8').readlines()]
    text_depart=jieba.cut(text.strip())
    outstr=''
    for word in text_depart:
        if word not in stopwords:
            if word !='\t':
                outstr+=word
                outstr+=" "
    return outstr