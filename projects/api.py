from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, UploadedFile, File
import jwt
from authtoken import AuthBearer

from accounts.models import Account
from resumes.models import Resume
from .models import Project as ProjectModel
from .schemas import Project, Error
from xxprod.settings import SECRET_KEY


router = Router()

@router.post('/create', response={201: Project, 401: Error}, auth=AuthBearer())
def create_project(request, project: Project, image_cover: UploadedFile = File(...)):
    resume = get_object_or_404(Resume, id=project.resume_id)
    new_project = ProjectModel.objects.create(name=project.name, description=project.description, resume=resume)
    new_project.image_cover.save(image_cover.name, image_cover)
    return 201, new_project

@router.get('/', response={200: List[Project], 401: Error}, auth=AuthBearer())
def get_projects(request, resume_id: int):
    resume = get_object_or_404(Resume, id=resume_id)
    projects = ProjectModel.objects.filter(resume=resume)
    return projects