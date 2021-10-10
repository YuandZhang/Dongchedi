# Dongchedi
懂车帝汽车热门车型评论爬虫

-目标网站 https://www.dongchedi.com/community/289/selected
前100个热门车型的评论
####首先爬取热门车型的id
- python Popluarcars_crawler.py

####爬取对应车型的精华评论并清洗数据
- python getComment.py

###requirements
- lxml==4.5.0
- jieba==0.42.1
- requests==2.22.0
- selenium==3.141.0
