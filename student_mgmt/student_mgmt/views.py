import os
from django.views.generic import View
from django.http import FileResponse
from .settings import BASE_DIR


class FileServeView(View):
    def get(self,*args, **kwargs):
        file_name = self.kwargs["file_name"]
        file_path = os.path.join(BASE_DIR, "static", "img", file_name)
        response = FileResponse(open(file_path, "rb"))
        return response