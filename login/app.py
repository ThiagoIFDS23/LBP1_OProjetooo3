from flask import Flask, redirect, url_for, session, request
from controllers import controller

app = Flask(__name__)
app.secret_key = 'chave-secreta'
app.register_blueprint(controller.msg)

@app.before_request
def inicio():
    if request.path == '/login':
        return
    
    if not 'nome' in session:
        return redirect(url_for('mensagens.login'))

if __name__ == '__main__':
    app.run(debug=True)