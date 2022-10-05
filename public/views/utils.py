from enum import Enum

from django.forms import Form, ModelForm
from django.http import JsonResponse


class HttpStatus(Enum):
    Ok = 200
    Redirect = 300
    BadRequest = 400
    NotFound = 404


def json_response(
    success: bool,
    message: str,
    data: dict | None = None,
    errors: list[str] | None = None,
    status: HttpStatus = HttpStatus.Ok,
) -> JsonResponse:
    if data is None:
        data = {}
    if errors is None:
        errors = []
    return JsonResponse(
        {"success": success, "message": message, "data": data, "errors": errors},
        status=status.value,
    )


def form_errors(form: Form | ModelForm) -> list[str]:
    error_list = []
    for title, errors in form.errors.get_json_data().items():
        title = " ".join([word.title() for word in title.split("_")])
        for error in errors:
            error_list.append(f"{title}: {error.get('message')}")
    return error_list
