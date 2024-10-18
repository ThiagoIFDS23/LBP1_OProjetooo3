from flask import Blueprint, session, render_template, redirect, url_for, request
from models import model

app = Blueprint('mensagens', __name__)
app.secret_key = 'chave-secreta'

@app.route('/')
def index():
    render_template('login.html')

@app.route('/bemvindo')
def bemvindo():
    render_template('index.html', nome=session['nome'])

@app.route('/login', methods=['POST', 'GET'])
def login():
    nome = request.form['nome']
    senha = request.form['senha']
    acesso = False

    if request.method == 'GET':
        if not nome in session:
            return render_template('login.html', acesso=acesso)
        else:
            return redirect(url_for('bemvindo'))
        
    if request.method == 'POST':
        for i in model.usuarios:
            if nome == i.nome and senha == i.senha:
                session['nome'] = nome
                session['senha'] = senha
                return redirect(url_for('bemvindo'))
        return render_template('login.html', acesso=acesso)
        
@app.route('/logout')
def logout():
    session.pop('nome', None)
    session.pop('senha', None)
    return redirect(url_for('index'))