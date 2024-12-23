from flask import Blueprint, session, render_template, redirect, url_for, request, make_response, flash
from models import tarefas
import json

lista = Blueprint('lista', __name__)

@lista.route('/', methods=['POST', 'GET'])
def index():
    id = int(request.cookies.get('total', '0'))
    if 'tarefas' not in session:
        session['tarefas'] = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        vencimento = request.form['vencimento']
        if not titulo or not descricao or not vencimento:
            flash('Campos não preenchidos', 'warning')    
            return redirect(url_for('lista.index'))
        else:
            flash('Tarefa enviada com sucesso', 'sucess')
        id += 1
        tarefas.add_Tarefa(session['tarefas'], id, titulo, descricao, vencimento) 
    resp = make_response(render_template('index.html', total=id))
    resp.set_cookie('total', str(id), max_age=60*60*24)
    return resp

@lista.route('/agenda')
def calendario():
    id = request.cookies.get('total')
    return render_template('agenda.html', total=id)

@lista.route('/deslogar')
def deslogar():
    resp = make_response(redirect(url_for('lista.index')))
    resp.set_cookie('total', '', expires=0)
    session.pop('tarefas', None)

    return resp

