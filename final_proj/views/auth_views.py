# 참고: https://wikidocs.net/81057
from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from final_proj import db
from final_proj.forms import RegisterForm
from final_proj.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register/', methods=('GET', 'POST'))
def register():
    # form = RegisterForm()

    # if request.method == 'POST' and form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
        
    #     if not user:
    #         user = User(username=form.username.data, 
    #                     password=generate_password_hash(form.password.data), # 암호화하여 전달
    #                     nickname=form.nickname.data)
        
    #         db.session.add(user)
    #         db.session.commit()

            # 회원가입 완료 후 메인 페이지로 리다이렉트
            # return redirect(url_for(''))
        #     return render_template('index.html')
        
        # else:
        #     flash('이미 존재하는 사용자입니다.')
        
        return render_template('registration.html')

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    return render_template('login.html')