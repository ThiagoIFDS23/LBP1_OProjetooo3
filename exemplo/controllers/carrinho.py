from flask import Blueprint, render_template, redirect, url_for, request, make_response
import json
from models import *

compra = Blueprint('carrinho', __name__)

@compra.route('/add')
def index():
    return render_template('abc.html')