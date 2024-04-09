# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from website import settings as website_settings
from django import http as django_http
import traceback
import logging
import typing
import utils
# endregion

# region			  -----Supporting Variables-----
logger = logging.getLogger(__file__)
# endregion

# endregion


class Process500Error(object):
    def __init__(self, get_response: typing.Callable)\
            -> None:
        self._get_response = get_response

    def __call__(self, request: typing.Dict)\
            -> typing.Dict:
        return self._get_response(request)

    def process_exception(self, request: django_http.HttpRequest,
                          exception: Exception)\
            -> django_http.JsonResponse:

        logger.error(traceback.format_exc())

        is_custom = isinstance(
            exception.__class__,
            utils.third_party.api.exceptions.ExtendedValidationError
        )
        if website_settings.DEBUG and is_custom:
            response_data = {"detail": _("Something went wrong"),
                             "success": False,
                             "traceback": traceback.format_exc().split("\n")}

            return django_http.JsonResponse(response_data,
                                            status=500)
        else:
            return None