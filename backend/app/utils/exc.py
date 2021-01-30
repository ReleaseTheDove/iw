
from fastapi import HTTPException


class FileNotFoundException(HTTPException):
    def __init__(self, detail: str):
        self.detail = f'File is not found:{detail}'
        self.status_code = 410
