from flask import Flask, render_template, redirect, url_for, request, session
from controllers import controllerLista

app = Flask(__name__)
app.register_blueprint(controllerLista.controller)
app.secret_key = 'supersecretkey'

@app.before_request
def inicio():
    if request.path == '/':
        return
    elif request.path == '/lista':
        if not 'tarefas' in session or session.get('viagens') == []:
            return redirect(url_for('lista.index'))
    else:
        return
    
    
@app.errorhandler(404)
def erro404(erro):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def erro(erro):
    return render_template('erro.html', mensagem=str(erro)), 500

if __name__ == '__main__':
    app.run(debug=True)