from flask import Flask

app = Flask(__name__)
nome = "Ezequiel"
idade = "15"
n1 = 12
n2 = 31

@app.route('/login')
def login():
    return f'<h1> Obrigado por acessar o sistema {nome}, sua idade é {idade} e você conseguiu entrar no sistema </h1>'

@app.route('/soma')
def soma():
    soma = n1 + n2
    return f'<h1> A soma é: {soma} </h1>'

@app.route('/subtração')
def subtração():
    subtração = n1 - n2
    return f'<h1> A subtração é: {subtração} </h1>'

@app.route('/multiplicação')
def multiplicação():
    multiplicação = n1 * n2
    return f'<h1> A multiplicação é: {multiplicação} </h1>'

@app.route('/divisão')
def divisão():
    divisão = n1 / n2
    return f'<h1> A divisão é: {divisão} </h1>'

if __name__ == "__main__":
    app.run(debug=True)
  
