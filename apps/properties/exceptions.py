"""
---------------------------
Exception to Properties app.
---------------------------
"""
from rest_framework.exceptions import APIException


class PropertyNotFound(APIException):
    """
    status_code = 404
    """

    status_code = 404
    default_detail = "The requested property was not found."
