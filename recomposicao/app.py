from flask import Flask
from controllers import controller

app = Flask(__name__)
app.register_blueprint(controller.produto)

if __name__ == '__main__':
    app.run(debug=True)