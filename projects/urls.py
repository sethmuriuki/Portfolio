from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$', views.index, name='portfolio'),
#  url(r'^image/(\d+)', views.single_photo, name = 'myimage'),
]
