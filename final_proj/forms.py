from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from final_proj.models import User

class RegisterForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('confirm_password', message='비밀번호가 일치하지 않습니다')])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired()])
    nickname = StringField('닉네임', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('회원가입')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('이미 존재하는 아이디입니다.')

    def validate_nickname(self, nickname):
        user = User.query.filter_by(nickname=nickname.data).first()
        if user:
            raise ValidationError('이미 존재하는 닉네임입니다.')

class LoginForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    submit = SubmitField('로그인')
