# Studash (학생 관리 대시보드)

FastAPI와 MongoDB를 기반으로 구축된 웹 기반 학생/선생님 관리 시스템입니다. 
학생의 성적, 동아리, 진로, 친한 친구 등의 정보를 관리하고, 성적을 시각화하여 보여줍니다.

## 기술 스택 (Tech Stack)

- **Backend**: Python 3, FastAPI
- **Database**: MongoDB (pymongo)
- **Frontend**: HTML5, Jinja2 Templates, Bootstrap 5, Chart.js
- **Server**: Uvicorn

## 프로젝트 구조 (Project Structure)
```text
studash/
├── main.py                     # FastAPI 앱 실행 및 설정 (Static Files 마운트 등)
├── router.py                   # 라우팅 및 API 엔드포인트 관리
├── services/
│   └── student_service.py      # MongoDB 데이터베이스 통신 및 비즈니스 로직
├── templates/                  # Jinja2 HTML 템플릿 폴더
│   ├── base.html               # 공통 레이아웃 (네비게이션, CDN 등)
│   ├── index.html              # 메인 페이지 (인원 등록 및 목록)
│   ├── detail.html             # 상세 페이지 (성적 그래프, 프로필 사진 업로드)
│   └── edit.html               # 정보 수정 페이지
└── app/static/profiles/        # 업로드된 프로필 이미지가 저장되는 로컬 폴더