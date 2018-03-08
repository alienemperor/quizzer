import sqlite3
import os, csv, random
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
    if ext not in '.csv':
        return "File extension not allowed."

    save_path = "tmp/{topic}".format(topic=topic)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path, overwrite=True)

    with open(file_path, "r") as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        for row in csvReader:
            c = conn.cursor()
            c.execute("INSERT INTO terms (topicid,term,definition) VALUES (?,?,?)", (top_id, row['term'], row['definition']))
            conn.commit()

    c.close()
    os.remove(file_path)
    return template('quiz_add', success=topic)


@route('/edit/<no:int>', method='GET')
def show_terms(no):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT term,definition FROM terms WHERE topicid LIKE ?", (str(no),))
    result = c.fetchall()
    d = conn.cursor()
    d.execute("SELECT topic FROM topics WHERE id LIKE ?", (str(no),))
    topic = d.fetchone()
    output = template('terms', rows=result, topic=topic)
    return output


@route('/quiz/<no:int>', method='POST')
@route('/quiz/<no:int>', method='GET')
def quiz_tests(no):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT term,definition FROM terms WHERE topicid LIKE ?", (str(no),))
    result = c.fetchall()
    d = conn.cursor()
    d.execute("SELECT topic FROM topics WHERE id LIKE ?", (str(no),))
    topic = d.fetchone()
    numQ = 25

    if len(result) < numQ:
        numQ = len(result)

    if request.POST:
        realans = []
        success = []
        resultans = []
        resultquest = []
        for x in range(1, (numQ+1)):
            ans = request.forms.get("Radios" + str(x))
            resultans.append(ans)
            quest = request.forms.get("Quest" + str(x))
            resultquest.append(quest)

            for i in result:
                if quest in i[0] and ans in i[1]:
                    realans.append(i[1])
                    success.append(True)
                elif quest in i[0] and ans not in i[1]:
                    realans.append(i[1])
                    success.append(False)

        return template('quiz_result', resultans=resultans, resultquest=resultquest, success=success, realans=realans)

    else:

        questions = random.sample(range(0, len(result)), numQ)

        return template('quiz', questions=questions, numQ=numQ, result=result, topic=topic, no=no)


run(host='192.168.100.222', port=8090, debug=True, reloader=True)