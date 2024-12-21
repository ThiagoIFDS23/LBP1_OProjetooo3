from flask import Blueprint, session, render_template, redirect, url_for, request, make_response, flash
from models import viagens
import json

controller = Blueprint('lista', __name__)

@controller.route('/', methods=['POST', 'GET'])
def index():
    id = int(request.cookies.get('total', '0'))
    sem_tarefas = False

    if 'viagens' not in session:
        session['viagens'] = []

    if request.method == 'POST':
        destino = request.form['destino']
        data = request.form['data']
        descricao = request.form['descricao']
        nota = request.form['nota']

        if not destino or not data or not descricao or not nota:
            flash('Campos não preenchidos', 'warning')    
            return redirect(url_for('lista.index'))
        else:
            flash('Viagem enviada com sucesso', 'sucess')

        id += 1
        viagens.add_Viagem(session['viagens'], id, destino, data, descricao, nota)

    resp = make_response(render_template('index.html', total=id))
    resp.set_cookie('total', str(id), max_age=60*60*24)
    return resp

@controller.route('/lista')
def calendario():
    id = request.cookies.get('total')
    return render_template('lista.html', total=id)

@controller.route('/deslogar')
def deslogar():
    resp = make_response(redirect(url_for('lista.index')))
    resp.set_cookie('total', '', expires=0)
    session.pop('viagens', None)
    return resp

