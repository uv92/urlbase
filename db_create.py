# -*- coding: utf-8 -*-
import MySQLdb

from config import DB_MAPPING

db = MySQLdb.connect(**DB_MAPPING)
with db:
    dbc = db.cursor()
    db.set_character_set('utf8')
    dbc.execute('SET NAMES utf8;')
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')
    try:
        dbc.execute(
            'drop table if EXISTS urls'
        )
        dbc.execute(
            'create table urls(url_id INT auto_increment,'
            'path TEXT not null,'
            'search_index TEXT not null,'
            'title VARCHAR (128),'
            'status BOOL not null,'
            'submission_date DATE not NULL,'
            'primary key (url_id)'
            ')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
        )
    except:pass
    # 0: read;
    # 1: to read
    dbc.execute(
        'INSERT into urls (path, search_index, title, submission_date, status)'
        'VALUES("https://www.zhihu.com/question/20336475", "Python源码推荐",'
        ' "初学 Python，有哪些 Pythonic 的源码推荐阅读？", "2017-03-01", 1) '
    )
    dbc.execute(
        'INSERT into urls (path, search_index, title, submission_date, status)'
        'VALUES("http://pythonpracticeprojects.com/", "Python项目",'
        ' "Python Practice Projects - Ideas for the Aspiring Developer","2017-04-14" ,0) '
    )
