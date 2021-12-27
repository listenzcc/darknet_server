import time
from django.shortcuts import render
from django.shortcuts import HttpResponse

from .settings import BASE_DIR
from .tool.get_pic import get_pic


def index(request):
    context = {}
    context['date'] = time.ctime()
    return render(request, 'index.html', context)


def pic_url(request):
    picUrl = request.get_full_path()[len(request.path)+1:]
    image_buffer = get_pic(picUrl)
    return HttpResponse(image_buffer, content_type="image/png")
