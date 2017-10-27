import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	#get a cursor object used to execute SQL commands
	c = connection.cursor()

	#create a table
	c.execute("""CREATE TABLE tasks
		(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL, due_date TEXT NOT NULL,
		priority INTEGER NOT NULL, status INTEGER NOT NULL
		)
		""")

	#Inserting dummmy data into the table
	c.execute("""INSERT INTO tasks (name,due_date,priority,status)
		VALUES('Finish Real Python Course 2', '11/25/2017', 10, 1)
		""")

	c.execute("""INSERT INTO tasks (name,due_date,priority,status)
		VALUES('Going for vacation in SA', '12/22/2017', 10, 1)
		""")
	
