import sqlite3
from functions import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for

#config
app = Flask(__name__)
app.config.from_object('_config')


#helper function
def db_connect():
	return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
	@wraps(test)
	def wrapper(*args, **kwarags):
		if 'logged_in' in session:
			return test(*args, **kwarags)
		else:
			flash('You need to log in first.')
			return redirect(url_for('login'))
	return wrapper

#route handlers

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Goodbye!')
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html', error=error)
		else:
			session['logged_in'] = True
			flash('Welcome!')
			return redirect(url_for('tasks'))
	return render_template('login.html')