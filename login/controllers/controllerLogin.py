from flask import Blueprint, session, render_template, redirect, url_for, request
from models import model

msg = Blueprint('mensagens', __name__)

@msg.route('/')
def index():
    return render_template('login.html')

@msg.route('/bemvindo')
def bemvindo():
    return render_template('bemvindo.html', nome=session['nome'])

@msg.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        for i in model.usuarios:
            if nome == i.nome and senha == i.senha:
                session['nome'] = nome
                session['senha'] = senha
                return redirect(url_for('mensagens.bemvindo'))
        return render_template('login.html', acesso=False)
        
    if request.method == 'GET':
        if not 'nome' in session:
            return render_template('login.html', acesso=True)
        else:
            return redirect(url_for('mensagens.bemvindo'))
        
@msg.route('/logout')
def logout():
    session.pop('nome', None)
    session.pop('senha', None)
    return redirect(url_for('mensagens.index'))