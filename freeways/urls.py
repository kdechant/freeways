from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^city/(?P<city_id>[0-9]+)$', views.api, name='api'),
]