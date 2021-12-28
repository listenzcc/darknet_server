import time
import pandas as pd

from django.shortcuts import render
from django.shortcuts import HttpResponse

from .settings import BASE_DIR, WallHaven_DIR
from .tool.get_pic import get_pic, mk_base64


def index(request):
    context = {}
    context['date'] = time.ctime()
    return render(request, 'index.html', context)


def explain_pic_url(request):
    # Explain the picture as the picUrl
    # print(request)
    print(request.GET)
    # picUrl = request.get_full_path()[len(request.path)+1:]
    picUrl = request.GET['picUrl']
    method = request.GET['method']
    print(picUrl, method)
    image_buffer, ext = get_pic(picUrl, method, WallHaven_DIR)
    return HttpResponse(image_buffer, content_type="image/{}".format(ext))


def list_wall_haven(request):
    # List all the thumb pictures,
    # and their fullSize partners.
    df = pd.read_csv(WallHaven_DIR.joinpath('assets.csv'))
    print(df)

    return HttpResponse(df.to_json(), content_type="json")


def get_wall_haven_thumb(request):
    # Get the buffer of the thumbnail picture of the name
    name = request.GET['thumbPic']
    path = WallHaven_DIR.joinpath('assets/_thumb').joinpath(name)
    image_buffer, ext = mk_base64(path)
    return HttpResponse(image_buffer, content_type="image/{}".format(ext))


def get_wall_haven_full_size(request):
    # Get the buffer of the fullSize picture of the name
    name = request.get_full_path()[len(request.path)+1:]
    path = WallHaven_DIR.joinpath('assets/_fullSize').joinpath(name)
