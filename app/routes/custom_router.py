from fastapi import APIRouter

class CustomRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "/kxoxxy"