from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/registration')
def register():
    return render_template('registertion.html')

@bp.route('/')
def index():
    return render_template('index.html')