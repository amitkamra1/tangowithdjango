from django.conf.urls import patterns, url
from rango import views

#patterns is from the django.conf.urls module
#When someone navigates to the page the urls.py is initiated
#The URL used is matched via the patterns & Url functions
#When a match happens the correct view is passed to the client

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'))