# 메모짱 (memojjang) 프로젝트

로컬 개발 환경 설정 및 실행 방법

1. 가상환경 생성 및 활성화

```
python -m venv .venv
source .venv/bin/activate
```

2. 의존성 설치

```
pip install -r requirements.txt
```

3. `.env` 파일 생성

```
cp .env.example .env
# 그리고 SECRET_KEY 등을 적절히 변경
```

4. 마이그레이션 및 서버 실행

```
python manage.py migrate
python manage.py runserver
```
