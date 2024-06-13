# 참고: https://wikidocs.net/81057
from flask import Blueprint, url_for, render_template, request, session, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from functools import wraps

from final_proj import db
from final_proj.forms import RegisterForm, LoginForm
from final_proj.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        # db에 유저가 없으면
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password.data), # pw를 해시 형태로 변환
                        nickname=form.nickname.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print('이미 존재하는 사용자입니다.')
    return render_template('registration.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            error = None
            user = User.query.filter_by(username=form.username.data).first()
            if not user:
                error = "존재하지 않는 사용자입니다."
            elif not check_password_hash(user.password, form.password.data):
                error = "비밀번호가 올바르지 않습니다."
            
            if error is None:
                session.clear()
                session['user_id'] = user.id
                return jsonify({'success': True, 'message':'로그인 성공'})
            else:
                return jsonify({'success': False, 'message': error})
        else:
            return jsonify({'success': False, 'message': '제출 폼이 유효하지 않습니다.'})
    elif request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        return jsonify({'success': False, 'message': 'Invalid request method'})
    
# 로그인 여부 확인
@bp.before_app_request
def is_login():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

# 로그인 되지 않았을 경우 로그인 페이지로 이동
# 데코레이터: 다른 함수를 인자로 받아, 그 함수에 새로운 기능을 덧붙여서 이를 반환하는 함수
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs): # 함수가 호출될 때 제공된 모든 키워드 인자를 캡처하여 함수 내에서 딕셔너리로 접근
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.route('/logout/')
def logout():
    session.clear()
    print('로그아웃 완료')
    return redirect(url_for('auth.login'))

# username, nickname 중복 검사
@bp.route('/check/username', methods=['POST'])
def check_username():
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    return jsonify({'exists': bool(user)})

@bp.route('/check/nickname', methods=['POST'])
def check_nickname():
    nickname = request.json.get('nickname')
    user = User.query.filter_by(nickname=nickname).first()
    return jsonify({'exists': bool(user)})