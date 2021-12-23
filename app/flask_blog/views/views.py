from flask_blog import app
from flask import redirect, request, url_for, render_template, flash, session
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method =='POST':
        if request.form['username']!=app.config['USERNAME']:
            flash('Username is different')
        elif request.form['password']!=app.config['PASSWORD']:
            flash('Password is different')
        else:
            session['logged_in']=True
            flash('Login successful')
            return redirect(url_for('show_entries'))
    #if GET method is called (GET method is default)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out!')
    return redirect(url_for('show_entries'))