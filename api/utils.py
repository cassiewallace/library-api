from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException


def library_exception_handler(exception, context=None):
        error = LibraryError(exception)
        response = error.format_response()

        return response


class LibraryError:
    def __init__(self, exception):
        self._exception = exception
        try:
            if isinstance(exception, APIException):
                self.status_code = exception.status_code
                self.code = exception.default_code
                self.message = exception.default_detail
                self.details = exception.get_full_details()
            else:
                self.status_code = exception.status_code
                self.code = exception.code
                self.message = exception.message
                self.details = exception.details
        except:
            self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.code = 'Internal Server Error'
            self.message = f'{exception}'
            self.details = exception.__dict__

    def format_response(self):
        data = {
            'code': self.code,
            'message': self.message,
            'details': self.details
        }
        headers = {}
        if getattr(self._exception, 'auth_header', None):
            headers['WWW-Authenticate'] = self._exception.auth_header
        if getattr(self._exception, 'wait', None):
            headers['Retry-After'] = f'{self._exception.wait}'

        return Response(data, status=self.status_code, headers=headers)