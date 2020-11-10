# Readme
This project is Flask that is python web framework of sample project.

# Project 구성
```
/yourapp
	/run.py
	/config.py
	/yourapp
		/__init__.py
		/views.py
		/models.py
		/static/
			/main.css
		/templates/
			/base.html
	/requirements.txt
	/yourappenv
```

### run.py
- 앱을 가져오고 개발 서버를 시작하는 실제 파이썬 코드를 포함합니다.
### config.py
- 앱 구성을 저장합니다.
### __init__.py
- Flask 응용 프로그램 인스턴스를 만드는 응용 프로그램을 초기화합니다.
### views.py
- 여기에서 경로가 정의됩니다.
### models.py
- 응용 프로그램에 대한 모델을 정의하는 곳입니다.
### static
- CSS, 자바 스크립트, 이미지 등의 정적 파일을 포함합니다.
### templates
- 여기에 html 템플릿 (예 : index.html, layout.html)을 저장합니다.
### requirements.txt
- 패키지 의존성을 저장하는 곳이며
### pip yourappenv
- 개발을위한 가상 환경

# Reference
https://wikidocs.net/78511