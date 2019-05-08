from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/workstest')
def workstest():
    return render_template('workstest.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
