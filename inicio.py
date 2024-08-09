# print("Alô Mundo!")
from flask import Flask, render_template 
from matematica import Matematica

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return "Olá Mundo!"

@app.route('/olamundo')
def mostrar():
    return render_template('pagina.html',titulo_dinamico='titulo ok')
@app.route('/listatimes')
def listar_times():
    lista = ['Flamengo','Palmeiras','Vasco']
    return render_template('listatimes.html',times=lista)

@app.route('/calculosoma')
def calcular():
    mat = Matematica(9,9)
    resposta = mat.somar()
    return render_template('calculo.html',resultado=resposta)

app.run()


