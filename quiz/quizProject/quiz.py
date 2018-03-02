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

@route('/add', method='POST')
def quiz_add():

        if request.POST.save:

            topic = request.POST.forms.get('topic')

            #conn = sqlite3.connect('quiz.db')
            #c = conn.cursor()

            #c.execute("INSERT INTO ")

            return "{topic}".format(topic=topic)
        else:
            return template('quiz_add')


@post('/')
def index():
    postdata = request.body.read()
    print postdata #this goes to log file only, not to client
    name = request.forms.get("name")
    surname = request.forms.get("surname")
    return "Hi {name} {surname}".format(name=name, surname=surname)


run(host='192.168.100.222', port=8000, debug=True, reloader=True)