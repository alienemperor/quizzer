import sqlite3
conn = sqlite3.connect('quiz.db') # Warning: This file is created in the current directory
#conn.execute("CREATE TABLE topics (id INTEGER PRIMARY KEY, topic char(100) NOT NULL)")
#conn.execute("DROP TABLE terms")
conn.execute("CREATE TABLE terms (id INTEGER PRIMARY KEY, topicid INTEGER, term char(100) NOT NULL, definition char(100) NOT NULL, FOREIGN KEY(topicid) REFERENCES topics(id))")
conn.commit()
