from flask import Flask, redirect, url_for, request
from controllers import carrinho, login

app = Flask(__name__)
app.register_blueprint(carrinho.compra)

@app.route("/")
def index():
    redirect(url_for('add'))

if __name__ == '__main__':
    app.run(debug=True)