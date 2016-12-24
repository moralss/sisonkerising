from django.conf.urls import url, include

from . import views
urlpatterns = [

        url(r'^home/$', views.index, name ='index'),
		url(r'^Contact/$', views.Contact, name ='Contact'),
        url(r'About/$', views.About, name ='About'),
      
]
