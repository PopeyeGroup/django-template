# region				-----External Imports-----
from rest_framework import (response as rest_response,
                            status as rest_status,
                            views as rest_views)
import typing
# endregion

# region				-----Internal Imports-----
# endregion

# region			  -----Supporting Variables-----
# endregion


class ExtendedValidationError(Exception):
    status_code: rest_status = rest_status.HTTP_400_BAD_REQUEST
    detail: str = None

    def __init__(self, detail: str,
                 status_code: rest_status)\
            -> None:
        self.status_code = status_code
        self.detail = detail


def custom_exception_handler(exc, context):
    if isinstance(exc, ExtendedValidationError):
        return rest_response.Response(data={"detail": exc.detail},
                                      status=exc.status_code)

    response = rest_views.exception_handler(exc, context)
    return response