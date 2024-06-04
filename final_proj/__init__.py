from flask import Flask, request, render_template
app = Flask(__name__) # 플라스크 어플리케이션 생성

@app.route('/')
def main():
    return render_template("login.html")

@app.route('/registration')
def test():
    return 'test중입니다.'

if __name__ == '__main__':
    app.run()