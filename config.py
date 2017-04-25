# -*- coding: utf-8 -*-
import os.path as op
basedir = op.abspath(op.dirname(__file__))

USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '^wlkl:#$+6yRdu#Es1fd3,4#m.1la'
DB_MAPPING = dict(
    host='10.211.55.11',
    user='root',
    passwd='wgzwgz',
    db='test1',
    connect_timeout=3500
)
