from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo_my_name='Rodrigo da Silva Souza')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
