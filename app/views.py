# -*- coding: utf-8 -*-
from functools import wraps

import MySQLdb as mdb
from Flask import Flask, flash, redirect, render_template, \
    request, session, url_for

# config
app = Flask(__name__)
app.config.from_object('config')

# helper func
def connect_db():
    return mdb.connect(**app.config['DB_MAPPING'])

def login_required(test):
    @wraps(test)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('请先登录')
            return redirect(url_for('login'))
    return wrapper

# router
@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash ('已登出')
    return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method = 'POST':
        if request.form['username'] != app.config['USERNAME'] \
            or request.form['password'] != app.config['PASSWORD']:
            error = '用户名无效或密码错误！'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('欢迎回来')
            return redirect(url_for('urls'))
    return render_template('login.html')
