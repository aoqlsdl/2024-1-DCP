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
├── static
│   ├── css
│   ├── icon
│   └── js
├── templates
├── venv // 가상환경
├── lib
│   └── api
├── img
├── pages
│   ├── Layout.jsx // 기본 페이지 레이아웃
│   ├── NavbarLayout.jsx // navbar를 포함한 페이지 레이아웃
│   └── routes.jsx // 중첩라우팅
└── styles // global style
```
