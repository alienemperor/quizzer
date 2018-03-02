import sqlite3
from bottle import route, run, template, request, error


@route('/')
@route('/quiz')
def quiz_home():

    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT id, topic FROM topics")
    result = c.fetchall()
    output = template('home.tpl', rows=result)
    return output


@route('/add')
def quiz_add():
    return template('quiz_add')


@route('/addTopic', method='POST')
def quiz_addtopic():
    topic = request.forms.get("topic")
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("INSERT INTO topics (topic) VALUES (?)", (topic,))

    conn.commit()
    c.close()

    alert = '<div class="alert alert-success alert-dismissible fade show" role="alert">' \
            '%s added to the database' \
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
            '<span aria-hidden="true">&times;</span>' \
            '</button>' \
            '</div>' % topic

    return template('quiz_add'), alert


run(host='192.168.100.222', port=8090, debug=True, reloader=True)