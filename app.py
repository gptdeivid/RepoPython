from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pymysql
from db_config import db

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

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
            return jsonify({'success': True, 'redirect': url_for('welcome')})
        else:
            return jsonify({'success': False, 'message': 'Credenciales inválidas'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Error en el servidor'})

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


