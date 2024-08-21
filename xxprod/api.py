from django.http import Http404
from ninja import NinjaAPI
from accounts.api import router as accounts_router
from django.db.utils import IntegrityError
from ninja.errors import ValidationError

from authtoken import InvalidToken
from hackathons.api import hackathon_router, my_hackathon_router
from profiles.api import router as profiles_router
from teams.api import team_router
from projects.api import router as projects_router
from resumes.api import router as resumes_router

api = NinjaAPI(
    title="Team Search",
    description="This is an API for team search."
)

api.add_router("/auth/", accounts_router)
api.add_router('/hackathons/', hackathon_router)
api.add_router('/myhackathons/', my_hackathon_router)
api.add_router('/', profiles_router)
api.add_router('/teams/', team_router)
api.add_router('/projects/', projects_router)
api.add_router('/resumes/', resumes_router)




@api.exception_handler(IntegrityError)
def integruty_error(request, exc):
    return api.create_response(
        request,
        {"details": f"Already exist: {exc}"},
        status=409
    )

@api.exception_handler(ValueError)
def value_error(request, exc):
    return api.create_response(
        request,
        {"details": f"Value is not valid: {exc}"},
        status=400
    )

@api.exception_handler(InvalidToken)
def invalid_token(request, exc):
    return api.create_response(
        request,
        {"details": "Provided token is not valid"},
        status=401
    )

@api.exception_handler(Http404)
def handle_404(request, exc):
    return api.create_response(
        request,
        {"details": "Not found or data is not correct"},
        status=400
    )

@api.exception_handler(ValidationError)
def handle_validation_error(request, exc):
    return api.create_response(
        request,
        {"details": f"Some data is not valid: {exc}"},
        status=400
    )