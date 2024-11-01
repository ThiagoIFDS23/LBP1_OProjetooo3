from flask import Blueprint, session, render_template, redirect, url_for, request
from models import model

msg = Blueprint('car', __name__)