from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
from db_config import db

import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# Cache busting
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    email = request.form['email']
    password = request.form['password']

    try:
        cursor = db.cursor()
        sql = "SELECT name FROM users WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['username'] = user[0]
            return redirect(url_for('welcome'))
        else:
            flash("Error de credenciales")
            return redirect(url_for('login'))
    except Exception as e:
        flash("Error de credenciales")
        return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


