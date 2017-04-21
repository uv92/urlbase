# -*- coding: utf-8 -*-
import MySQLdb

db = MySQLdb.connect(user='root', passwd='******', db='test1', connect_timeout=3000)
with db:
    dbc = db.cursor()
    db.set_character_set('utf8')
    dbc.execute('SET NAMES utf8;')
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')
    try:
        dbc.execute(
            'create table urls(url_id INT not NULL auto_increment,'
            'path TEXT not null,'
            'search_index TEXT not null,'
            'title VARCHAR (128),'
            'status BOOL not null,'
            'primary key (url_id)'
            ')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
        )
    except:pass
    # 0: read;
    # 1: to read
    dbc.execute(
        'INSERT into urls (path, search_index, title, status)'
        'VALUES("https://www.zhihu.com/question/20336475", "Python源码推荐",'
        ' "初学 Python，有哪些 Pythonic 的源码推荐阅读？", 1) '
    )
    dbc.execute(
        'INSERT into urls (path, search_index, title, status)'
        'VALUES("http://pythonpracticeprojects.com/", "Python项目",'
        ' "Python Practice Projects - Ideas for the Aspiring Developer", 0) '
    )
