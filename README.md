> 디지털콘텐츠프로그래밍 기말프로젝트 레포지토리입니다.

<br>

## Start Project

```
# Project Setup Instructions

## Clone the repository
git clone https://github.com/aoqlsdl/2024-1-DCP.git
cd final_proj

## Setup virtual environment
# On Windows
python -m venv venv
venv\Scripts\activate

# On MacOS/Linux
python3 -m venv venv
source venv/bin/activate

## install dependencies
pip install -r requirements.txt

## setup environmental variables
## 먼저, final_proj 폴더 내에 .env 파일을 생성한 후, 아래의 텍스트를 붙여넣습니다. 보안상 SECRET_KEY를 공개하면 안되지만, 부득이하게 SECRET_KEY를 문서에 작성하는 점 양해 부탁드립니다.
SECRET_KEY=58wS77oICFxM0T7K

## initialize database
flask db upgrade

## run the server
flask run
```

## Stacks

### Language & Framework

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">

### Database

<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

## Folder Structure

```
/final_proj
├── static # 정적 파일을 보관하는 디렉토리
│   ├── css
│   ├── icon
│   └── js
├── templates/ # Flask의 템플릿 파일들을 저장하는 디렉토리
├── venv/ # 가상환경
├── views/ # 애플리케이션의 뷰 함수를 정의한 파이썬 스크립트 파일들을 보관하는 디렉토리, 이때 뷰 함수는 클라이언트의 요청을 받아서 처리하고, 결과를 반환하는 역할
├── __init.py__ # Flask 애플리케이션의 시작점으로, 애플리케이션을 생성하고 구성하는 코드를 포함함
├── config.py # 애플리케이션의 구성 설정을 포함하는 파일
├── forms.py # 폼과 폼 검증을 위한 WTForms 라이브러리의 폼 클래스를 정의하는 파일
├── models.py # 데이터베이스의 모델을 정의하는 파일
├── pybo.py # SQLite 데이터베이스 파일
└── requirements.txt # 필요한 Python 패키지 및 라이브러리의 목록을 포함하는 파일
```
