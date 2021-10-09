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
from utils.Configuration import Config
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

def seg_tail_split(str1, sep=r":|,|，|。|n|！|!|：|'\'"):  # 分隔符可为多样的正则表达式
    # 保留分割符号，置于句尾，比如标点符号
    wlist = re.split(sep, str1)
    seg_word = re.findall(sep, str1)
    seg_word.extend(" ")  # 末尾插入一个空字符串，以保持长度和切割成分相同
    wlist = [x + y for x, y in zip(wlist, seg_word)]  # 顺序可根据需求调换
    return wlist

def ListCharReplace(ls,o,n):
    #x:需要的列表
    #o:原来的字符
    #n:现在的字符
    b = list(ls[0])
    rep = [n if x == o else x for x in b]
    s =["".join(rep)]
    return s