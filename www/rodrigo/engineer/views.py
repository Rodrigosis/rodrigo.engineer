from flask import Flask, render_template, request

from www.rodrigo.engineer import trigger_email

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
        issuer_name = request.form['contato_nome']
        subject = request.form['contato_assunto']
        message_body = request.form['contato_mensagem']
        sender = request.form['contato_email']

        email_header = issuer_name + ' - ' + subject

        trigger_email.TriggerEmail(app).submit(email_header, message_body, sender, ['rodrigo.sis.s7@gmail.com'])

    # trigger_email.TriggerEmail(app).submit()

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


if __name__ == '__main__':
    app.debug = True
    app.run()
