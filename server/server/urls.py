"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.staticfiles.views import serve

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('index.html', views.index),
    path('favicon.ico', serve, {'path': 'icon/favicon.ico'}),

    re_path(r'^explainPic/get/$', views.explain_pic_url),

    re_path(r'^listWallHaven/json/$', views.list_wall_haven),
    re_path(r'^wallHavenThumb/get/$', views.get_wall_haven_thumb)
]
