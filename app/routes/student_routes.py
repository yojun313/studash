from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.student_service import StudentService
import shutil
import os
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

PROFILE_DIR = "app/static/profiles"

@router.get("/", response_class=HTMLResponse)
async def list_students(request: Request):
    students = StudentService.get_all_students()
    # 최신 FastAPI/Starlette 방식: request를 키워드 인자로 전달
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"students": students}
    )

@router.post("/upload-profile/{student_id}")
async def upload_profile_picture(student_id: str, profile_pic: UploadFile = File(...)):
    # 1. 파일 확장자 추출 (예: .jpg, .png)
    extension = Path(profile_pic.filename).suffix
    
    # 2. 저장할 파일 이름 지정 (학생 ID를 이름으로 써서 중복 방지 및 덮어쓰기)
    filename = f"{student_id}{extension}"
    file_path = os.path.join(PROFILE_DIR, filename)

    # 3. 로컬 폴더에 실제 파일 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(profile_pic.file, buffer)

    # 4. DB에 이미지 URL 경로 업데이트
    # 브라우저에서 접근할 때는 /static/profiles/파일명 으로 접근
    image_url = f"/static/profiles/{filename}"
    StudentService.update_student(student_id, {"profile_url": image_url})

    # 업로드 후 다시 상세 페이지로 이동
    return RedirectResponse(url=f"/student/{student_id}", status_code=303)

@router.post("/add")
async def add_student(
    name: str = Form(...),
    role: str = Form(...),  # ✅ 구분(선생님/학생) 추가
    midterm: int = Form(...),
    final: int = Form(...),
    personality: str = Form(...),
    career: str = Form(...),
    club: str = Form(...),
    best_friend: str = Form("")
):
    student_data = {
        "name": name,
        "role": role,       # ✅ 데이터베이스에 저장할 딕셔너리에 추가
        "grades": {"midterm": midterm, "final": final},
        "personality": personality,
        "career": career,
        "club": club,
        "best_friend": best_friend
    }
    StudentService.create_student(student_data)
    return RedirectResponse(url="/", status_code=303)


@router.post("/edit/{student_id}")
async def edit_student(
    student_id: str,
    name: str = Form(...),
    role: str = Form(...),  # ✅ 구분 추가
    midterm: int = Form(...),
    final: int = Form(...),
    personality: str = Form(...),
    career: str = Form(...),
    club: str = Form(...),
    best_friend: str = Form("")
):
    student_data = {
        "name": name,
        "role": role,       # ✅ 업데이트할 데이터에 추가
        "grades": {"midterm": midterm, "final": final},
        "personality": personality,
        "career": career,
        "club": club,
        "best_friend": best_friend
    }
    StudentService.update_student(student_id, student_data)
    return RedirectResponse(url=f"/student/{student_id}", status_code=303)

@router.get("/student/{student_id}", response_class=HTMLResponse)
async def student_detail(request: Request, student_id: str):
    student = StudentService.get_student_by_id(student_id)
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"student": student}
    )

# --- 학생 정보 수정 폼 페이지 렌더링 ---
@router.get("/edit/{student_id}", response_class=HTMLResponse)
async def edit_student_form(request: Request, student_id: str):
    student = StudentService.get_student_by_id(student_id)
    return templates.TemplateResponse(
        request=request,
        name="edit.html",
        context={"student": student}
    )