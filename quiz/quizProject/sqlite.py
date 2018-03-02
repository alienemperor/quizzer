import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE topics (id INTEGER PRIMARY KEY, topic char(100) NOT NULL)")
conn.execute("CREATE TABLE terms (id INTEGER PRIMARY KEY, term char(100) NOT NULL, definition char(100) NOT NULL)")
conn.commit()
