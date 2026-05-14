# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

TaskFlow — 업무 추가·삭제·상태 변경 기능을 갖춘 풀스택 업무 관리 웹앱

## 기술 스택

- **백엔드**: FastAPI + SQLAlchemy + SQLite (`backend/`)
- **프론트엔드**: Vanilla JS + Tailwind CDN (`frontend/`)

## 개발 명령어

```powershell
# 백엔드 서버 실행 (http://localhost:8000)
cd backend
uvicorn main:app --reload

# 프론트엔드 — 브라우저에서 직접 열기
start frontend\index.html

# 의존성 설치
pip install -r requirements.txt

# API 문서 (서버 실행 후)
# http://localhost:8000/docs
```

## 아키텍처

```
backend/
  main.py       # FastAPI 앱 및 모든 라우트 (/api/tasks)
  database.py   # SQLAlchemy 엔진, 세션, get_db 의존성
  models.py     # Task 모델 (id, title, status, created_at)
  schemas.py    # Pydantic 스키마 (Create / Update / Response)
frontend/
  index.html    # SPA — fetch API로 백엔드 직접 호출
```

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/api/tasks` | 전체 업무 조회 |
| POST | `/api/tasks` | 업무 추가 |
| PATCH | `/api/tasks/{id}` | 상태 변경 (`todo` / `in_progress` / `done`) |
| DELETE | `/api/tasks/{id}` | 업무 삭제 |

## 코딩 규칙

- 한국어 주석 사용
- 변수명: `snake_case` (Python), `camelCase` (JS)
- jQuery 사용 금지 / CSS 직접 작성 금지 (Tailwind만 사용)
