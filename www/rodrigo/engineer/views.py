import os
from flask import Flask, render_template, request

from www.rodrigo.engineer.trigger_email import TriggerEmail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo_my_name='Rodrigo da Silva Souza')


@app.route('/about')
def about():
    return render_template('sobre.html')


@app.route('/projects')
def projects():
    return render_template('projetos.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        issuer_name = request.form['name']
        subject = request.form['subject']
        message_body = request.form['message']
        sender = request.form['email']

        TriggerEmail(app).submit(issuer_name, message_body, sender, subject)

    return render_template('contato.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/curriculum')
def curriculum():
    return render_template('curriculo.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
