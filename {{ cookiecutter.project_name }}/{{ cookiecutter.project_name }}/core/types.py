from django.http import HttpRequest
from {{ cookiecutter.project_name }}.users.models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User