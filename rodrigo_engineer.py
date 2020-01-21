from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    topicos = ['Física', 'Química', 'Cálculo', 'Elétrica', 'Eletrônica', 'IoT', 'AI',
               'Python', 'Java', 'JavaScript', 'HTML/CSS', 'Arquitetura de software']

    return render_template('index.html', titulo_my_name='Rodrigo da Silva Souza', lista=topicos)


app.run(debug=True)
