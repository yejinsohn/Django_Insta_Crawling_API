# Django_Insta_Crawling_API


## 가상환경
### 가상환경 생성
```
python -m venv [가상환경 이름]
```

### 가상환경 실행
```
[가상환경 이름]/scripts/activate
```

### 가상환경 비활성화
```
deactivate
```

## 프로젝트 세팅 (가상환경 내부에 설치)
### Django 설치
```
pip install Django
```

### 패키지 설치
```
pip install djangorestframework
```

### Django 프로젝트 생성
```
django-admin startproject [프로젝트 이름] .
```

### Django 앱 생성
```
python manage.py startapp [앱이름]
```

## 서버 실행 (marge.py가 있는 디렉토리에서 작업)
### 모델 변경사항 감지 및 기록
```
python manage.py makemigrations
```

### 변경사항을 DB에 적용
```
python manage.py migrate
```

### 서버 실행
```
python manage.py runserver
```

## 패키지
### 설치한 패키지를 한번에 받기
```
pip install -r requirements.txt
```
