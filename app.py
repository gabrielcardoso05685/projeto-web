from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')
def inicio():
    return '<h1>Olá, Mundo!</h1>'

@app.route('/sobre')
def sobre():
    return '''
<h1 style='color:red'>Meu nome: </h1>
<p>Matheus Gonzaga <b> da Costa </b>
<!-- Tudo que eu pensar em html pode vir aqui --> </p>
'''
@app.route('/ronan')
def ronan():
    return '''
<h1 style='background-color:red'>Ronan</h1>
'''

@app.route('/var')
def variavel():
    palavra = 'Ronan'
    return f'<h1>Adicionando texto de var: {palavra}' #f = texto formatado, pode receber variaveis

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Voce tem {calculoIdade}'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/arquivo')
def arquivo():
    return '''
<h1>Criando uma página nova com uma rota nova
<p>:)</p>
'''

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = "Maior de idade"
    elif idade == 18:
        status = "Maior de idade"
    else:
        status = "Menor de idade - ACESSO NEGADO"

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4,
    }
    return render_template('dicio.html', **dados)

@app.route('/condicao')
def condicao():
    numero = {
        'chave' : 'valor',
        'numero' : 10,
    }
    return render_template('condicao.html', **numero)

@app.route('/testando/<int:numero>')
def testando(numero):
    return render_template('condicao.html', numero = numero)

@app.route('/perfil/<nome>')
def perfil(nome):
    usuarios = {
        'admin': {
            'nome': 'Administrador',
            'email': 'admin@fatec.br',
            'nivel': 'administrador',
            'ativo': True,
            'posts': 47
        },
        'joao': {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'nivel': 'usuario',
            'ativo': True,
            'posts': 12
        },
        'maria': {
            'nome': 'Mario Souza',
            'email': 'maria@email.com',
            'nivel': 'moderador',
            'ativo': False,
            'posts': 31
        },
    }

    usuario = usuarios.get(nome)
    return render_template('perfil.html', usuario = usuario, nome_buscado = nome)














#ultima coisa do arquivo








if __name__ == '__main__':
    app.run(debug=True)