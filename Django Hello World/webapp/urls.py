from django.conf.urls import url

from . import views

urlpatterns = [
       url (r'^$', views.index, name = 'index') #index starts and ends pattern(nothing in between)
    ]
