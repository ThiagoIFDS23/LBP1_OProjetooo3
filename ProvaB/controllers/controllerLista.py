from flask import Blueprint, session, render_template, redirect, url_for, request, make_response, flash
from models import tarefas
import json

lista = Blueprint('lista', __name__)

@lista.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form:
            flash('Tarefa enviada com sucesso', 'sucess')
        else:
            flash('Campos não preenchidos', 'error')    
            return redirect(url_for(lista.index))
        
        tarefas.id += 1
        tarefas.add_Tarefa(tarefas.id, request.form['titulo'], request.form['descricao'], request.form['vencimento']) 
        session['tarefas'] = tarefas.tarefas
    resp = make_response(render_template('index.html', total=tarefas.id))
    resp.set_cookie('total', json.dumps(tarefas.id), max_age=60*60*24)
    return resp

@lista.route('/agenda')
def calendario():
    cookie = json.loads(request.cookies.get('total'))
    return render_template('agenda.html', total=cookie)

@lista.route('/deslogar')
def deslogar():
    tarefas.id = 0
    resp = make_response(redirect(url_for('lista.index')))
    resp.set_cookie('total', '', expires=0)
    session.pop('tarefas', None)

    return resp

