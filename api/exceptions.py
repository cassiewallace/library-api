from rest_framework import exceptions, status


class LibraryException(Exception):

    def __init__(self, message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        code='Internal Server Error', details=None):
        self.status_code = status_code
        self.code = code
        self.message = message
        self.details = details


class BookCheckedOutException(LibraryException):

    def __init__(self, details=None):
        super().__init__(
            message='This book is already checked out.',
            status_code=status.HTTP_403_FORBIDDEN,
            code='Book Already Checked Out',
            details=details
        )


class BookCheckedInException(LibraryException):

    def __init__(self, details=None):
        super().__init__(
            message='This book is already checked in.',
            status_code=status.HTTP_403_FORBIDDEN,
            code='Book Already Checked In',
            details=details
        )