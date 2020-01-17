from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template.html', titulo_my_name='Rodrigo da Silva Souza')


app.run()
