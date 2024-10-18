from flask import Flask, redirect, url_for, session
from controllers import controller

app = Flask(__name__)
app.register_blueprint(controller.app)

@app.before_request
def inicio():
    if not 'nome' in session:
        return redirect(url_for('controller.login'))

if __name__ == '__main__':
    app.run(debug=True)