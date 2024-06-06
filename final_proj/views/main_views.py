from flask import Blueprint, render_template
from final_proj.forms import RegisterForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')