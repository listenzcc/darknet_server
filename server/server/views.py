import time
import pandas as pd

from django.shortcuts import render
from django.shortcuts import HttpResponse

from .settings import BASE_DIR, WallHaven_DIR
from .tool.get_pic import get_pic, mk_buffer


def index(request):
    context = {}
    context['date'] = time.ctime()
    return render(request, 'index.html', context)


def parse_pic_url(request):
    # Parse the picture as the picUrl
    print(request)
    picUrl = request.get_full_path()[len(request.path)+1:]
    image_buffer, ext = get_pic(picUrl)
    return HttpResponse(image_buffer, content_type="image/{}".format(ext))


def list_wall_haven_thumb(request):
    # List all the thumb pictures,
    # and their fullSize partners.
    # !!! It is an very **unsafe** matching method
    files = [e.name for e in WallHaven_DIR.joinpath('assets/_thumb').iterdir()]
    files_full = [e.name for e in WallHaven_DIR.joinpath(
        'assets/_fullSize').iterdir()]

    df = pd.DataFrame(files, columns=['thumb'])
    df['fullSize'] = files_full

    print(df)
    return HttpResponse(df.to_json(), content_type="json")


def get_wall_haven_thumb(request):
    # Get the buffer of the thumbnail picture of the name
    name = request.get_full_path()[len(request.path)+1:]
    path = WallHaven_DIR.joinpath('assets/_thumb').joinpath(name)
    image_buffer, ext = mk_buffer(path)
    return HttpResponse(image_buffer, content_type="image/{}".format(ext))


def get_wall_haven_full_size(request):
    # Get the buffer of the fullSize picture of the name
    name = request.get_full_path()[len(request.path)+1:]
    path = WallHaven_DIR.joinpath('assets/_fullSize').joinpath(name)
