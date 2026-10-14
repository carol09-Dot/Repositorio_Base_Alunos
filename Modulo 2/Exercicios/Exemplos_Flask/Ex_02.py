from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return "Olá, mundo!"

@app.route('/sobre')
def sobre():
    return "Olá, me chamo Carol, e sou vicíada em café e jogos"

@app.route("/ola/<nome>")
def ola(nome):
    return f"Olá {nome}! seja bem-vindo(a)"

@app.route("/dobro/<int:numero>")
def dobro(numero):
    return f"O dobro de {numero} é {numero*2}"

if __name__ == '__main__':
    app.run(debug=True)