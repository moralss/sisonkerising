from django.conf.urls import url , include

from . import views

urlpatterns = [
    url(r'play/',views.play, name = 'play'),
    url(r'^$',views.index, name = 'index'),
    ]
