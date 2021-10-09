# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 16:39
# @Author  : yumh
# @Site    : Shenyang
# @File    : getComment.py
# @Software: PyCharm
import requests
from lxml import etree
from lxml import html
import csv
from utils.prepare_data import *

def getcarid():
    caridls=[]
    carnamels=[]
    with open('data/carinfo.csv',encoding='utf-8') as cf:
        lines=cf.readlines()
        for line in lines:
            carid, carname=line.split(',')[0],line.split(',')[1]
            caridls.append(carid)
            carnamels.append(carname)
        return caridls,carnamels



def getUrl(carid):
    url='https://www.dongchedi.com/community/{}/selected'.format(carid)
    return url

def getRoot(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'}
    r=requests.get(url,headers=headers)
    # etree=html.etree
    root=etree.HTML(r.text)
    return root

def getComment(root,url,carid,carname):
    #pages //*[@id="__next"]/div[1]/div[2]/div[3]/div[2]/div[4]/ul
    #text1 //*[@id="__next"]/div[1]/div[2]/div[3]/div[2]/div[3]/section[6]/div[2]/p/a/span/text()
    # //*[@id="__next"]/div[1]/div[2]/div[3]/div[2]/div[3]/section[7]/div[2]/p/a/span/text()
    pages=root.xpath('//*[@id="__next"]/div[1]/div[2]/div[3]/div[2]/div[4]/ul/li')
    pages=len(pages)-2#获取页面个数
    commentls=[]
    for p in range(1,pages+1):

        _url=url+'-{}'.format(str(p))
        root=getRoot(_url)
        CommentRoot=root.xpath('//*[@id="__next"]/div[1]/div[2]/div[3]/div[2]/div[3]/section')
        for comment in CommentRoot:
            comment=comment.xpath('./div[2]/p/a/span/text()')
            if len(comment)==0:
                continue#判断是否为空
            commentls.append(comment)

    saveComment(commentls,carid,carname,'csv')

def saveComment(commentls,carid,carname,filetype):

    if filetype=='csv':
        for i in range(0, len(commentls)):
            with open('data/carcomment_2.csv','a',encoding='utf-8',newline='') as dc:
                rep_comment=ListCharReplace(commentls[i],'{','(')
                dcwriter = csv.writer(dc, delimiter='{')
                dcwriter.writerow([carid,carname,commentls[i]])
    elif filetype=='txt':
        for i in range(0, len(commentls)):
            with open('data/carcomment.txt', mode='a', encoding='utf-8', newline='') as dc:
                dc.writelines(carid+'||||'+carname+'||||'+commentls[i])

def Spider():
    caridls,carnamels=getcarid()

    for c in range(0,len(caridls)):
        print('正在爬取第{}辆车'.format(str(c)))
        carid=caridls[c]
        carname=carnamels[c]#当前爬取的车型
        url = getUrl(carid)
        root = getRoot(url)
        getComment(root, url,carid,carname)

def TidyComment():
    originfile='data/carcomment_2.csv'
    tidyfile='data/carcomment_cleaned.txt'
    textid=1
    with open(originfile, mode='r', encoding='utf-8', newline='')as ofile:
        with open(tidyfile,mode='a',encoding='utf-8')as tfile:
            lines=ofile.readlines()
            for line in lines:
                sen_ls=[]
                senid=1
                carid=line.split('{')[0]
                carname=line.split('{')[1]
                carcomment=line.split('{')[2][1:-2]
#分割文本-去停用词-

                split_comment_ls=seg_tail_split(carcomment)#分割成句子列表

                print('正在写入{}'.format(str(textid)))
                for sen in split_comment_ls:
                    sen=remove_stopwords(sen)
                    if len(sen)!=0:
                        sen_ls.append(sen)#生成新的句子列表sen_ls
                sen_len=len(sen_ls)#子句列表长度
                tfile.writelines(str(textid) + sen_len+'\n')  # 写入文本序号,子句个数
                tfile.writelines(carid + ',' + carname + '\n')  # 写入车ID，车辆名称
                for _sen in sen_ls:
                    tfile.writelines(str(senid)+','+_sen+'\n')
                    senid=senid+1
                textid=textid+1







if __name__ == '__main__':
    # Spider()
    TidyComment()
