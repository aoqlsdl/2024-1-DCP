from flask import Blueprint, render_template
from final_proj.views.auth_views import login_required

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
@login_required # 데코레이터 적용
def index():
    return render_template('index.html')