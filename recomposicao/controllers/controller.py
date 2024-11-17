from flask import Blueprint, render_template, redirect, url_for, request
from models import model

produto = Blueprint('produto', __name__)

@produto.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    produtos = []
    if page == 1:
        for i in range(0, 3):
            produtos.append(model.produtos[i])

    if page == 2:
        for i in range(3, 6):
            produtos.append(model.produtos[i])

    if page == 3:
        for i in range(6, 9):
            produtos.append(model.produtos[i])

    if page == 4:
        produtos.append(model.produtos[9])

    return render_template("index.html", produtos=produtos, page=page)