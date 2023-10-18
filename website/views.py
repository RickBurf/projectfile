from flask import Blueprint, render_template
from . import db


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create')
def create():
    return render_template('create.html')

@bp.route('/history')
def history():
    return render_template('history.html')

@bp.route('/sevents')
def sevents():
    return render_template('SEVENTS.html')
