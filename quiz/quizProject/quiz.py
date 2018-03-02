import sqlite3
from bottle import route, run, template, request, error


@route('/')
@route('/quiz')
def quiz_home():

    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT topic FROM topics")
    result = c.fetchall()
    output = template('home.tpl', rows=result)
    return output


@route('/add')
def quiz_add():
    return template('quiz_add')


@route('/addTopic', method='POST')
def quiz_addtopic():
    topic = request.forms.get("topic")
    return "{topic}".format(topic=topic)


run(host='192.168.100.222', port=8090, debug=True, reloader=True)