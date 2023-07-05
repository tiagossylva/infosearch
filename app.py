from flask import Flask,render_template
from consultas_bd import *
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
def create_app(app):
    app.config['MYSQL_HOST'] = 'containers-us-west-52.railway.app'
    app.config['MYSQL_PORT'] = 6828
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'gkHs0eh4YYx6zBKa8SX4'
    app.config['MYSQL_DB'] = 'railway'
    app.config['MYSQL_DATABASE'] = 'railway'
    mysql = MySQL(app)
    return mysql
connection = create_app(app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/consulta')
def cosulta():
    return render_template("consulta.html")


@app.route('/search', methods=['POST'])
def search():
    estado = request.form.get('estado')
    combustivel = request.form.get('combustivel')

    dados = diesel(connection)
    dados_json = json.dumps(dados)
    dados2 = diesel_s10(connection)
    dados_json2 = json.dumps(dados2)
    dados3 = etanol(connection)
    dados_json3 = json.dumps(dados3)
    dados4 = gasolina(connection)
    dados_json4 = json.dumps(dados4)
    dados5 = gnv(connection)
    dados_json5 = json.dumps(dados5)

    if estado == f"{estado}" and combustivel == "diesel":
        opcao = "valor1"
    elif estado == f"{estado}" and combustivel == "diesels10":
        opcao = "valor2"
    elif estado == f"{estado}" and combustivel == "etanol":
        opcao = "valor3"
    elif estado == f"{estado}" and combustivel == "gasolina":
        opcao = "valor4"
    elif estado == f"{estado}" and combustivel == "gnv":
        opcao = "valor5"


    elif estado == "selecione" and combustivel =="diesel":
        opcao = "valor5"


    else:
        opcao = "nenhum valor"
    return render_template('consulta.html',
                           estado=estado,
                           opcao=opcao,
                           dados=dados_json,
                           dados2=dados_json2,
                           dados3=dados_json3,
                           dados4=dados_json4,
                           dados5=dados_json5
                           )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')



if __name__ == '__main__':
    app.run(debug=True)