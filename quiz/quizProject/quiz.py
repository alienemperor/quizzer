import sqlite3
import os, csv
from bottle import route, run, template, request, error, static_file


@route('/')
@route('/home')
def quiz_home():

    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT id, topic FROM topics")
    result = c.fetchall()
    output = template('home.tpl', rows=result)
    return output


@route('/add')
def quiz_add():
    return template('quiz_add', success=None)


@route('/addTopic', method='POST')
def quiz_addtopic():
    topic = request.forms.get("topic")
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("INSERT INTO topics (topic) VALUES (?)", (topic,))
    top_id = c.lastrowid

    conn.commit()


    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.csv'):
        return "File extension not allowed."

    save_path = "tmp/{topic}".format(topic=topic)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)

    with open(file_path) as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        for row in csvReader:
            c.execute("INSERT INTO terms (topicid,term,definition) VALUES (?,?,?)", (top_id, row['term'], row['definition']))

    c.close()
    return template('quiz_add', success=topic)


@route('/quiz')
def quiz_tests():

    return template('quiz.tpl')


run(host='192.168.100.222', port=8090, debug=True, reloader=True)