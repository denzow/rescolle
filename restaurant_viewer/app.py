# coding: utf-8

"""
WIP

bottleでWEB画面つくりたい
"""

from bottle import route, run, template


@route('/')
@route('/index')
def index():
    return template('index', hello=100)


if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)
