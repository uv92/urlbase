# -*- coding: utf-8 -*-
from functools import wraps

import MySQLdb as mdb
from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, g

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

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
            or request.form['password'] != app.config['PASSWORD']:
            error = '用户名无效或密码错误！'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('欢迎回来')
            return redirect(url_for('urls'))
    return render_template('login.html')

@app.route('/urls/')
@login_required
def urls():
    g.db = connect_db()
    curs = g.db.execute(
        'select search_index, title, submission_date, path where status = 1'
    )
    to_read = [dict(search_index=row[0],
                    title=row[1],
                    submission_date=row[2],
                    path=row[3])
               for row in curs.fetchall()]

    curs = g.db.execute(
        'select search_index, title, submission_date, path where status = 0'
    )
    read = [dict(search_index=row[0],
                    title=row[1],
                    submission_date=row[2],
                    path=row[3])
               for row in curs.fetchall()]
    g.db.close()
    return render_template(
        'urls.html',
        to_read=to_read,
        read=read,
        form=AddUrlForm(request.form)
    )

@app.route('/add/', methods=['POST'])
@login_required
def add_url():
    g.db = connect_db()
    search_index = request.form['search_index']
    path = request.form['path']
    status = request.form['status']

