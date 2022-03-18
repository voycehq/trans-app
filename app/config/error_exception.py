from fastapi import status


class ErrorException(Exception):
    def __init__(self, error: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.error = error
        self.status = status_code
        self.message = error
