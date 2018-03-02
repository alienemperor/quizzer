import sqlite3
from bottle import route, run, template, request, error

@route('/')
@route('/quiz')
def quiz_home():

    if request.POST.save:

        new = request.POST.task.strip()
        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()

        c.execute